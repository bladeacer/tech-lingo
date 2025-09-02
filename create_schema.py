#!/usr/bin/env python3
import os
import yaml

def get_yml_files(directory):
    """
    Recursively finds all valid .yml files that do not start with a '_'.
    """
    file_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.yml') and not file.startswith('_'):
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
        matches = extract_matches_from_file(file)
        all_entries.extend(matches)

    # Sort the entries alphabetically by the 'trigger' key
    all_entries.sort(key=lambda x: x['trigger'].lower())

    # --- New Feature: Variant Status Table (now at the top) ---
    
    # Get all unique triggers for quick lookup
    all_triggers = {entry['trigger'] for entry in all_entries}
    
    # Extract a list of all unique lowercase base triggers
    base_triggers = sorted(list({get_base_trigger(t).lower() for t in all_triggers}))

    # Add the heading and table headers for the new table
    markdown_content = "# Espanso Package Schema\n\n"
    markdown_content += "## Trigger Variant Status\n\n"
    markdown_content += "This table shows which case and source variants are defined for each trigger.\n\n"
    markdown_content += "| Base Trigger | `_` | `_wk-` | `_tl-` |\n"
    markdown_content += "| :--- | :---: | :---: | :---: |\n"
    
    # Iterate through the base triggers and check for all 9 variants
    for base in base_triggers:
        # Generate the three case variations
        lower = base
        title = base.title()
        upper = base.upper()

        # Check for existence of each variant and generate status icons
        base_status = "✓" if f"_{lower}" in all_triggers and f"_{title}" in all_triggers and f"_{upper}" in all_triggers else "✗"
        wk_status = "✓" if f"_wk-{lower}" in all_triggers and f"_wk-{title}" in all_triggers and f"_wk-{upper}" in all_triggers else "**✗**"
        tl_status = "✓" if f"_tl-{lower}" in all_triggers and f"_tl-{title}" in all_triggers and f"_tl-{upper}" in all_triggers else "**✗**"

        # Append a new row to the table
        markdown_content += f"| `{base}` | {base_status} | {wk_status} | {tl_status} |\n"
        
    # --- Main Table (now below the variant status table) ---
    
    markdown_content += "\n\n## All Triggers and Expansions\n\n"
    markdown_content += "This document lists all triggers and their corresponding expansions from the YAML files in this package.\n\n"
    markdown_content += "| Trigger | Expansion |\n"
    markdown_content += "| :--- | :--- |\n"
    
    for entry in all_entries:
        escaped_replace = entry['replace'].replace('|', '\|')
        markdown_content += f"| `{entry['trigger']}` | {escaped_replace} |\n"

    # Write the combined content to schema.md
    try:
        with open('schema.md', 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print("Successfully generated schema.md file.")
    except Exception as e:
        print(f"Failed to write schema.md: {e}")

if __name__ == "__main__":
    create_schema_md()

