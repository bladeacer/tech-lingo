#!/usr/bin/env python3
import os
import yaml
import time
import webbrowser
import threading
import http.server
import socketserver
import socket

# --- File Handling Functions ---

def get_yml_files(directory):
    """
    Recursively finds all valid .yml files to process.
    """
    file_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            is_valid = False
            # Check for standard files
            if file.endswith('.yml') and not file.startswith('_'):
                is_valid = True
            # Check for files with the new allowed prefixes
            elif file.endswith('.yml') and (file.startswith('__') or file.startswith('_u-') or file.startswith('_')):
                is_valid = True
            
            if is_valid:
                file_paths.append(os.path.join(root, file))
    return file_paths

def extract_matches_from_file(filepath):
    """
    Extracts 'trigger' and 'replace' matches from a single YAML file.
    """
    entries = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            if data and 'matches' in data:
                for match in data['matches']:
                    if 'trigger' in match and 'replace' in match:
                        trigger = match['trigger'].strip()
                        replace = match['replace'].strip().replace('\n', ' ')
                        entries.append({'trigger': trigger, 'replace': replace})
    except yaml.YAMLError as e:
        print(f"Error reading YAML file {filepath}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred with file {filepath}: {e}")
    return entries

def get_base_trigger(trigger):
    """
    Extracts the base name of a trigger by removing known prefixes.
    """
    if trigger.startswith('_wk-'):
        return trigger[4:]
    elif trigger.startswith('_tl-'):
        return trigger[4:]
    elif trigger.startswith('_u-'):
        return trigger[3:]
    elif trigger.startswith('__'):
        return trigger[2:]
    elif trigger.startswith('_'):
        return trigger[1:]
    return trigger

def create_schema_md():
    """
    Orchestrates the process of reading YAML files, extracting triggers,
    and writing them to a schema.md file in a Markdown table.
    """
    all_entries = []
    
    # Get all valid YAML file paths
    yml_files = get_yml_files(os.getcwd())
    
    # Extract matches from each file and compile a single list
    for file in yml_files:
        print(f"Processing file: {file}")
        matches = extract_matches_from_file(file)
        all_entries.extend(matches)

    # Sort the entries alphabetically by the 'trigger' key
    all_entries.sort(key=lambda x: x['trigger'].lower())

    # --- Variant Status Table ---
    
    all_triggers = {entry['trigger'] for entry in all_entries}
    base_triggers = sorted(list({get_base_trigger(t).lower() for t in all_triggers}))
    print(f"\nFound {len(all_triggers)} total triggers.")
    print(f"Unique base triggers: {base_triggers}")


    markdown_content = "# Espanso Package Schema\n\n"
    markdown_content += "## Trigger Variant Status\n\n"
    markdown_content += "This table shows which case and source variants are defined for each trigger.\n\n"
    markdown_content += "| Base Trigger | `_` | `_wk-` | `_tl-` | `__` | `_u-` |\n"
    markdown_content += "| :--- | :---: | :---: | :---: | :---: | :---: |\n"
    
    for base in base_triggers:
        lower = base
        title = base.title()
        upper = base.upper()

        # Debugging: show which variants are being checked
        print(f"\nChecking variants for base trigger: `{base}`")
        print(f"  _ variants: `_{lower}`, `_{title}`, `_{upper}` (Found: {f'_{lower}' in all_triggers}, {f'_{title}' in all_triggers}, {f'_{upper}' in all_triggers})")
        print(f"  _wk- variants: `_wk-{lower}`, `_wk-{title}`, `_wk-{upper}` (Found: {f'_wk-{lower}' in all_triggers}, {f'_wk-{title}' in all_triggers}, {f'_wk-{upper}' in all_triggers})")
        print(f"  _tl- variants: `_tl-{lower}`, `_tl-{title}`, `_tl-{upper}` (Found: {f'_tl-{lower}' in all_triggers}, {f'_tl-{title}' in all_triggers}, {f'_tl-{upper}' in all_triggers})")
        print(f"  __ variants: `__{lower}`, `__{title}`, `__{upper}` (Found: {f'__{lower}' in all_triggers}, {f'__{title}' in all_triggers}, {f'__{upper}' in all_triggers})")
        print(f"  _u- variants: `_u-{lower}`, `_u-{title}`, `_u-{upper}` (Found: {f'_u-{lower}' in all_triggers}, {f'_u-{title}' in all_triggers}, {f'_u-{upper}' in all_triggers})")


        base_status = "✓" if f"_{lower}" in all_triggers and f"_{title}" in all_triggers and f"_{upper}" in all_triggers else "**✗**"
        wk_status = "✓" if f"_wk-{lower}" in all_triggers and f"_wk-{title}" in all_triggers and f"_wk-{upper}" in all_triggers else "**✗**"
        tl_status = "✓" if f"_tl-{lower}" in all_triggers and f"_tl-{title}" in all_triggers and f"_tl-{upper}" in all_triggers else "**✗**"
        double_status = "✓" if f"__{lower}" in all_triggers and f"__{title}" in all_triggers and f"__{upper}" in all_triggers else "**✗**"
        u_status = "✓" if f"_u-{lower}" in all_triggers and f"_u-{title}" in all_triggers and f"_u-{upper}" in all_triggers else "**✗**"

        markdown_content += f"| `{base}` | {base_status} | {wk_status} | {tl_status} | {double_status} | {u_status} |\n"
        
    # --- Main Table ---
    
    markdown_content += "\n\n## All Triggers and Expansions\n\n"
    markdown_content += "This document lists all triggers and their corresponding expansions from the YAML files in this package.\n\n"
    markdown_content += "| Trigger | Expansion |\n"
    markdown_content += "| :--- | :--- |\n"
    
    for entry in all_entries:
        escaped_replace = entry['replace']
        markdown_content += f"| `{entry['trigger']}` | {escaped_replace} |\n"

    # Write the combined content to schema.md
    try:
        with open('schema.md', 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print("\nSuccessfully generated schema.md file.")
    except Exception as e:
        print(f"\nFailed to write schema.md: {e}")

# --- File Polling Logic ---

def get_file_state(directory):
    """
    Returns a dictionary mapping file paths to their modification times.
    Correctly includes files that start with '__' or '_u-'.
    """
    state = {}
    for root, _, files in os.walk(directory):
        for file in files:
            is_valid = False
            # Check for standard files
            if file.endswith('.yml') and not file.startswith('_'):
                is_valid = True
            # Check for files with the new allowed prefixes
            elif file.endswith('.yml') and (file.startswith('__') or file.startswith('_u-') or file.startswith('_')):
                is_valid = True
            
            if is_valid:
                filepath = os.path.join(root, file)
                try:
                    state[filepath] = os.path.getmtime(filepath)
                except OSError:
                    continue
    return state

# --- Web Server and Threading ---

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map['.js'] = 'application/javascript'
Handler.extensions_map['.css'] = 'text/css'

if __name__ == "__main__":
    # Run the function once at startup to create the initial file
    create_schema_md()

    # Find an available port to start the server
    httpd = None
    port_range = range(8000, 8010)
    for port in port_range:
        try:
            httpd = socketserver.TCPServer(("", port), Handler)
            print(f"Serving at http://localhost:{port}")
            break
        except socket.error as e:
            print(f"Port {port} is in use, trying next one...")
            continue
    
    if httpd is None:
        print("Could not find an available port in the range 8000-8009. Please close any other running servers.")
    else:
        # Start the web server in a separate thread
        server_thread = threading.Thread(target=httpd.serve_forever)
        server_thread.start()

        # Open the HTML file in the default browser
        print("Opening schema preview in your default browser...")
        webbrowser.open_new_tab(f"http://localhost:{port}/index.html")

        # Get the initial state of the files
        last_state = get_file_state('.')

        print("\nStarting file watcher... Press Ctrl+C to stop.")
        try:
            while True:
                time.sleep(2)  # Check for changes every 2 seconds
                current_state = get_file_state('.')

                # Check for changes
                files_changed = False
                
                # Check for new or modified files
                for filepath, mtime in current_state.items():
                    if filepath not in last_state:
                        print(f"\nDetected new file: {filepath}")
                        files_changed = True
                    elif mtime != last_state[filepath]:
                        print(f"\nDetected a change to: {filepath}")
                        files_changed = True

                # Check for deleted files
                for filepath in last_state:
                    if filepath not in current_state:
                        print(f"\nDetected a deleted file: {filepath}")
                        files_changed = True

                if files_changed:
                    create_schema_md()

                # Update the state for the next check
                last_state = current_state

        except KeyboardInterrupt:
            print("\nWatcher stopping...")
            httpd.shutdown()
            server_thread.join()
            print("Watcher stopped.")

