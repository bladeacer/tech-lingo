# Espanso Package Schema

## Trigger Variant Status

This table shows which case and source variants are defined for each trigger.

| Base Trigger | `_` | `_wk-` | `_tl-` |
| :--- | :---: | :---: | :---: |
| `ack` | ✓ | ✓ | ✓ |
| `ag` | ✓ | ✓ | ✓ |
| `awk` | ✓ | ✓ | ✓ |
| `emaclient` | ✓ | ✓ | ✓ |
| `emacs` | ✓ | ✓ | ✓ |
| `fsf` | ✓ | ✓ | ✓ |
| `gawk` | ✓ | ✓ | ✓ |
| `gh` | ✓ | ✓ | ✓ |
| `git` | ✓ | ✓ | ✓ |
| `glab` | ✓ | ✓ | ✓ |
| `grep` | ✓ | ✓ | ✓ |
| `gvim` | ✓ | ✓ | ✓ |
| `ls` | ✓ | ✓ | ✓ |
| `nvim` | ✓ | ✓ | ✓ |
| `pwd` | ✓ | ✓ | ✓ |
| `rg` | ✓ | ✓ | ✓ |
| `ssh` | ✓ | ✓ | ✓ |
| `svn` | ✓ | ✓ | ✓ |
| `vdiff` | ✓ | ✓ | ✓ |
| `vim` | ✓ | ✓ | ✓ |
| `vtutor` | ✓ | ✓ | ✓ |


## All Triggers and Expansions

This document lists all triggers and their corresponding expansions from the YAML files in this package.

| Trigger | Expansion |
| :--- | :--- |
| `_ack` | A search tool like grep, optimized for developers. |
| `_Ack` | A search tool like grep, optimized for developers. Related to: rg, which is much faster. |
| `_ACK` | A search tool like grep, optimized for developers. Related to: rg, which is much faster.  More information: https://beyondgrep.com/documentation. |
| `_ag` | ag, the Silver Searcher. |
| `_Ag` | ag, the Silver Searcher. Like ack, but aims to be faster. |
| `_AG` | ag, the Silver Searcher. Like ack, but aims to be faster.  More information: https://manned.org/ag. |
| `_awk` | awk is a versatile programming language for working on files. |
| `_Awk` | awk is a versatile programming language for working on files. Note: Different implementations of AWK often make this a symlink of their binary. Related to: gawk. |
| `_AWK` | awk is a versatile programming language for working on files. Note: Different implementations of AWK often make this a symlink of their binary. Related to: gawk.  More information: https://github.com/onetrueawk/awk. |
| `_emaclient` | emacsclient lets you open files in an existing Emacs server. |
| `_Emaclient` | emacsclient lets you open files in an existing Emacs server. Related to: emacs. |
| `_EMACLIENT` | emacsclient lets you open files in an existing Emacs server. Related to: emacs.  More information: https://www.gnu.org/software/emacs/manual/html_node/emacs/emacsclient-Options.html. |
| `_emacs` | emacs is an extensible, customizable, self-documenting, real-time display editor. |
| `_Emacs` | emacs is an extensible, customizable, self-documenting, real-time display editor. Related to: emacsclient. |
| `_EMACS` | emacs is an extensible, customizable, self-documenting, real-time display editor. Related to: emacsclient.  More information: https://www.gnu.org/software/emacs. |
| `_fsf` | The Free Software Foundation (FSF) is a non-profit organisation which supports the free software movement with its preference for software being distributed under copyleft terms. |
| `_Fsf` | The Free Software Foundation (FSF) is a non-profit organisation founded by Richard Stallman.  The organisation supports the free software movement, with its preference for software being distributed under copyleft ('share alike') terms. For more information: https://en.wikipedia.org/wiki/Free_Software_Foundation. |
| `_FSF` | The Free Software Foundation (FSF) is a 501(c)(3) non-profit organisation founded by Richard Stallman on October 4, 1985.  The organisation supports the free software movement, with its preference for software being distributed under copyleft ('share alike') terms, such as with its own GNU General Public License. For more information: https://en.wikipedia.org/wiki/Free_Software_Foundation. |
| `_gawk` | GNU version of awk, a versatile programming language for working on files. |
| `_Gawk` | GNU version of awk, a versatile programming language for working on files. Related to: awk. |
| `_GAWK` | GNU version of awk, a versatile programming language for working on files. Related to: awk.  More information: https://www.gnu.org/software/gawk/manual/gawk.html. |
| `_gh` | gh is a CLI for GitHub. |
| `_Gh` | gh is a Command Line Interface (CLI) which works seamlessly with GitHub. Some subcommands such as config have their own usage documentation. |
| `_GH` | gh is a Command Line Interface (CLI) which works seamlessly with GitHub. Some subcommands such as config have their own usage documentation.  More information: https://cli.github.com/manual/gh. |
| `_git` | git is a distributed version control system. |
| `_Git` | git is a distributed version control system. Some common subcommands include commit, add, branch, switch, push. |
| `_GIT` | git is a distributed version control system. Some common subcommands include commit, add, branch, switch, push.  More information: https://git-scm.com/docs/git. |
| `_glab` | glab is a CLI for GitLab. |
| `_Glab` | glab is a Command Line Interface (CLI) which works seamlessly with GitLab. Some subcommands such as config have their own usage documentation. |
| `_GLAB` | glab is a Command Line Interface (CLI) which works seamlessly with GitLab. Some subcommands such as config have their own usage documentation.  More information: https://gitlab.com/gitlab-org/cli/-/tree/main/docs/source. |
| `_grep` | grep can be used to find patterns in files using regexes. |
| `_Grep` | grep is a CLI tool which can be used to find patterns in files using regexes (regular expressions). |
| `_GREP` | grep is a CLI tool which can be used to find patterns in files using regexes (regular expressions).  More information: https://www.gnu.org/software/grep/manual/grep.html. |
| `_gvim` | gvim is a Graphical User Interface version of Vim (Vi IMproved), a command-line text editor. |
| `_Gvim` | gvim is a Graphical User Interface (GUI) version of Vim (Vi IMproved), a command-line text editor.  Related to: vimdiff, vimtutor, nvim, vim. |
| `_GVIM` | gvim is a Graphical User Interface version of Vim (Vi IMproved), a command-line text editor.  Related to: vimdiff, vimtutor, nvim, vim. More information: https://www.vim.org. |
| `_ls` | List directory contents (ls) |
| `_Ls` | List directory contents.  More information: https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html. |
| `_LS` | List directory contents.  More information: https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html. |
| `_nvim` | Neovim is a programmer's text editor based on Vim. |
| `_Nvim` | Neovim is a programmer's text editor based on Vim, which provides several modes for different kinds of text manipulation. |
| `_NVIM` | Neovim is a programmer's text editor based on Vim, which provides several modes for different kinds of text manipulation.  Pressing <i> in normal mode enters insert mode. <Esc> or <Ctrl c> goes back to normal mode, which doesn't allow regular text insertion.  Related to: vim, vimtutor, vimdiff. More information: https://neovim.io. |
| `_pwd` | Print the name of current/working directory (pwd). |
| `_Pwd` | Print the name of current/working directory (pwd).  More information: https://www.gnu.org/software/coreutils/manual/html_node/pwd-invocation.html. |
| `_PWD` | Print the name of current/working directory (pwd).  More information: https://www.gnu.org/software/coreutils/manual/html_node/pwd-invocation.html. |
| `_rg` | ripgrep, a recursive line-oriented search tool. |
| `_Rg` | ripgrep, a recursive line-oriented search tool. Aims to be a faster alternative to grep. |
| `_RG` | ripgrep, a recursive line-oriented search tool. Aims to be a faster alternative to grep.  More information: https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md. |
| `_ssh` | Secure Shell (SSH) |
| `_Ssh` | Secure Shell (SSH) is a protocol used to securely log onto remote systems. It can be used for logging or executing commands on a remote server.. |
| `_SSH` | Secure Shell is a protocol used to securely log onto remote systems. It can be used for logging or executing commands on a remote server.  More information: https://man.openbsd.org/ssh. |
| `_svn` | svn is a Subversion client tool. |
| `_Svn` | svn is a Subversion client tool.  More information: https://svnbook.red-bean.com/en/1.7/svn-book.html#svn.ref.svn. |
| `_SVN` | svn is a Subversion client tool.  More information: https://svnbook.red-bean.com/en/1.7/svn-book.html#svn.ref.svn. |
| `_tl-ack` | A search tool like grep, optimized for developers. |
| `_tl-Ack` | A search tool like grep, optimized for developers. Related to: rg, which is much faster. |
| `_tl-ACK` | A search tool like grep, optimized for developers. Related to: rg, which is much faster.  More information: https://beyondgrep.com/documentation. |
| `_tl-ag` | ag, the Silver Searcher. |
| `_tl-Ag` | ag, the Silver Searcher. Like ack, but aims to be faster. |
| `_tl-AG` | ag, the Silver Searcher. Like ack, but aims to be faster.  More information: https://manned.org/ag. |
| `_tl-awk` | awk is a versatile programming language for working on files. |
| `_tl-Awk` | awk is a versatile programming language for working on files. Note: Different implementations of AWK often make this a symlink of their binary. Related to: gawk. |
| `_tl-AWK` | awk is a versatile programming language for working on files. Note: Different implementations of AWK often make this a symlink of their binary. Related to: gawk.  More information: https://github.com/onetrueawk/awk. |
| `_tl-emaclient` | emacsclient lets you open files in an existing Emacs server. |
| `_tl-Emaclient` | emacsclient lets you open files in an existing Emacs server. Related to: emacs. |
| `_tl-EMACLIENT` | emacsclient lets you open files in an existing Emacs server. Related to: emacs.  More information: https://www.gnu.org/software/emacs/manual/html_node/emacs/emacsclient-Options.html. |
| `_tl-emacs` | emacs is an extensible, customizable, self-documenting, real-time display editor. |
| `_tl-Emacs` | emacs is an extensible, customizable, self-documenting, real-time display editor. Related to: emacsclient. |
| `_tl-EMACS` | emacs is an extensible, customizable, self-documenting, real-time display editor. Related to: emacsclient.  More information: https://www.gnu.org/software/emacs. |
| `_tl-fsf` | The Free Software Foundation (FSF) is a non-profit organisation which supports the free software movement with its preference for software being distributed under copyleft terms. |
| `_tl-Fsf` | The Free Software Foundation (FSF) is a non-profit organisation founded by Richard Stallman.  The organisation supports the free software movement, with its preference for software being distributed under copyleft ('share alike') terms. For more information: https://en.wikipedia.org/wiki/Free_Software_Foundation. |
| `_tl-FSF` | The Free Software Foundation (FSF) is a 501(c)(3) non-profit organisation founded by Richard Stallman on October 4, 1985.  The organisation supports the free software movement, with its preference for software being distributed under copyleft ('share alike') terms, such as with its own GNU General Public License. For more information: https://en.wikipedia.org/wiki/Free_Software_Foundation. |
| `_tl-gawk` | GNU version of awk, a versatile programming language for working on files. |
| `_tl-Gawk` | GNU version of awk, a versatile programming language for working on files. Related to: awk. |
| `_tl-GAWK` | GNU version of awk, a versatile programming language for working on files. Related to: awk.  More information: https://www.gnu.org/software/gawk/manual/gawk.html. |
| `_tl-gh` | gh is a CLI for GitHub. |
| `_tl-Gh` | gh is a Command Line Interface (CLI) which works seamlessly with GitHub. Some subcommands such as config have their own usage documentation. |
| `_tl-GH` | gh is a Command Line Interface (CLI) which works seamlessly with GitHub. Some subcommands such as config have their own usage documentation.  More information: https://cli.github.com/manual/gh. |
| `_tl-git` | git is a distributed version control system. |
| `_tl-Git` | git is a distributed version control system. Some common subcommands include commit, add, branch, switch, push. |
| `_tl-GIT` | git is a distributed version control system. Some common subcommands include commit, add, branch, switch, push.  More information: https://git-scm.com/docs/git. |
| `_tl-glab` | glab is a CLI for GitLab. |
| `_tl-Glab` | glab is a Command Line Interface (CLI) which works seamlessly with GitLab. Some subcommands such as config have their own usage documentation. |
| `_tl-GLAB` | glab is a Command Line Interface (CLI) which works seamlessly with GitLab. Some subcommands such as config have their own usage documentation.  More information: https://gitlab.com/gitlab-org/cli/-/tree/main/docs/source. |
| `_tl-grep` | grep can be used to find patterns in files using regexes. |
| `_tl-Grep` | grep is a CLI tool which can be used to find patterns in files using regexes (regular expressions). |
| `_tl-GREP` | grep is a CLI tool which can be used to find patterns in files using regexes (regular expressions).  More information: https://www.gnu.org/software/grep/manual/grep.html. |
| `_tl-gvim` | gvim is a Graphical User Interface version of Vim (Vi IMproved), a command-line text editor. |
| `_tl-Gvim` | gvim is a Graphical User Interface (GUI) version of Vim (Vi IMproved), a command-line text editor.  Related to: vimdiff, vimtutor, nvim, vim. |
| `_tl-GVIM` | gvim is a Graphical User Interface version of Vim (Vi IMproved), a command-line text editor.  Related to: vimdiff, vimtutor, nvim, vim. More information: https://www.vim.org. |
| `_tl-ls` | List directory contents (ls) |
| `_tl-Ls` | List directory contents.  More information: https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html. |
| `_tl-LS` | List directory contents.  More information: https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html. |
| `_tl-nvim` | Neovim is a programmer's text editor based on Vim. |
| `_tl-Nvim` | Neovim is a programmer's text editor based on Vim, which provides several modes for different kinds of text manipulation. |
| `_tl-NVIM` | Neovim is a programmer's text editor based on Vim, which provides several modes for different kinds of text manipulation.  Pressing <i> in normal mode enters insert mode. <Esc> or <Ctrl c> goes back to normal mode, which doesn't allow regular text insertion.  Related to: vim, vimtutor, vimdiff. More information: https://neovim.io. |
| `_tl-pwd` | Print the name of current/working directory (pwd). |
| `_tl-Pwd` | Print the name of current/working directory (pwd).  More information: https://www.gnu.org/software/coreutils/manual/html_node/pwd-invocation.html. |
| `_tl-PWD` | Print the name of current/working directory (pwd).  More information: https://www.gnu.org/software/coreutils/manual/html_node/pwd-invocation.html. |
| `_tl-rg` | ripgrep, a recursive line-oriented search tool. |
| `_tl-Rg` | ripgrep, a recursive line-oriented search tool. Aims to be a faster alternative to grep. |
| `_tl-RG` | ripgrep, a recursive line-oriented search tool. Aims to be a faster alternative to grep.  More information: https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md. |
| `_tl-ssh` | Secure Shell (SSH) |
| `_tl-Ssh` | Secure Shell (SSH) is a protocol used to securely log onto remote systems. It can be used for logging or executing commands on a remote server.. |
| `_tl-SSH` | Secure Shell is a protocol used to securely log onto remote systems. It can be used for logging or executing commands on a remote server.  More information: https://man.openbsd.org/ssh. |
| `_tl-svn` | svn is a Subversion client tool. |
| `_tl-Svn` | svn is a Subversion client tool.  More information: https://svnbook.red-bean.com/en/1.7/svn-book.html#svn.ref.svn. |
| `_tl-SVN` | svn is a Subversion client tool.  More information: https://svnbook.red-bean.com/en/1.7/svn-book.html#svn.ref.svn. |
| `_tl-vdiff` | vimdiff opens up two or more files in vim and show the differences between them. |
| `_tl-Vdiff` | vimdiff open up two or more files in vim and show the differences between them. Related to: vim, vimtutor, nvim. |
| `_tl-VDIFF` | Open up two or more files in vim and show the differences between them. Related to: vim, vimtutor, nvim.  More information: https://www.vim.org. |
| `_tl-vim` | Vim (Vi IMproved) is a command-line text editor. |
| `_tl-Vim` | Vim (Vi IMproved) is a command-line text editor, provides several modes for different kinds of text manipulation. |
| `_tl-VIM` | Vim (Vi IMproved) is a command-line text editor, provides several modes for different kinds of text manipulation. Pressing <i> in normal mode enters insert mode. Pressing <Esc> goes back to normal mode, which enables the use of Vim commands.  Related to: vimdiff, vimtutor, nvim, gvim. More information: https://www.vim.org. |
| `_tl-vtutor` | vimtutor teaches the basic vim commands. |
| `_tl-Vtutor` | vimtutor teaches the basic vim commands. Related to: vim, vimdiff, nvim. |
| `_tl-VTUTOR` | vimtutor teaches the basic vim commands. Related to: vim, vimdiff, nvim.  More information: https://manned.org/vimtutor. |
| `_vdiff` | vimdiff opens up two or more files in vim and show the differences between them. |
| `_Vdiff` | vimdiff open up two or more files in vim and show the differences between them. Related to: vim, vimtutor, nvim. |
| `_VDIFF` | Open up two or more files in vim and show the differences between them. Related to: vim, vimtutor, nvim.  More information: https://www.vim.org. |
| `_vim` | Vim (Vi IMproved) is a command-line text editor. |
| `_Vim` | Vim (Vi IMproved) is a command-line text editor, provides several modes for different kinds of text manipulation. |
| `_VIM` | Vim (Vi IMproved) is a command-line text editor, provides several modes for different kinds of text manipulation. Pressing <i> in normal mode enters insert mode. Pressing <Esc> goes back to normal mode, which enables the use of Vim commands.  Related to: vimdiff, vimtutor, nvim, gvim. More information: https://www.vim.org. |
| `_vtutor` | vimtutor teaches the basic vim commands. |
| `_Vtutor` | vimtutor teaches the basic vim commands. Related to: vim, vimdiff, nvim. |
| `_VTUTOR` | vimtutor teaches the basic vim commands. Related to: vim, vimdiff, nvim.  More information: https://manned.org/vimtutor. |
| `_wk-ack` | A search tool like grep, optimized for developers. |
| `_wk-Ack` | A search tool like grep, optimized for developers. Related to: rg, which is much faster. |
| `_wk-ACK` | A search tool like grep, optimized for developers. Related to: rg, which is much faster.  More information: https://beyondgrep.com/documentation. |
| `_wk-ag` | ag, the Silver Searcher. |
| `_wk-Ag` | ag, the Silver Searcher. Like ack, but aims to be faster. |
| `_wk-AG` | ag, the Silver Searcher. Like ack, but aims to be faster.  More information: https://manned.org/ag. |
| `_wk-awk` | awk is a versatile programming language for working on files. |
| `_wk-Awk` | awk is a versatile programming language for working on files. Note: Different implementations of AWK often make this a symlink of their binary. Related to: gawk. |
| `_wk-AWK` | awk is a versatile programming language for working on files. Note: Different implementations of AWK often make this a symlink of their binary. Related to: gawk.  More information: https://github.com/onetrueawk/awk. |
| `_wk-emaclient` | emacsclient lets you open files in an existing Emacs server. |
| `_wk-Emaclient` | emacsclient lets you open files in an existing Emacs server. Related to: emacs. |
| `_wk-EMACLIENT` | emacsclient lets you open files in an existing Emacs server. Related to: emacs.  More information: https://www.gnu.org/software/emacs/manual/html_node/emacs/emacsclient-Options.html. |
| `_wk-emacs` | emacs is an extensible, customizable, self-documenting, real-time display editor. |
| `_wk-Emacs` | emacs is an extensible, customizable, self-documenting, real-time display editor. Related to: emacsclient. |
| `_wk-EMACS` | emacs is an extensible, customizable, self-documenting, real-time display editor. Related to: emacsclient.  More information: https://www.gnu.org/software/emacs. |
| `_wk-fsf` | The Free Software Foundation (FSF) is a non-profit organisation which supports the free software movement with its preference for software being distributed under copyleft terms. |
| `_wk-Fsf` | The Free Software Foundation (FSF) is a non-profit organisation founded by Richard Stallman.  The organisation supports the free software movement, with its preference for software being distributed under copyleft ('share alike') terms. For more information: https://en.wikipedia.org/wiki/Free_Software_Foundation. |
| `_wk-FSF` | The Free Software Foundation (FSF) is a 501(c)(3) non-profit organisation founded by Richard Stallman on October 4, 1985.  The organisation supports the free software movement, with its preference for software being distributed under copyleft ('share alike') terms, such as with its own GNU General Public License. For more information: https://en.wikipedia.org/wiki/Free_Software_Foundation. |
| `_wk-gawk` | GNU version of awk, a versatile programming language for working on files. |
| `_wk-Gawk` | GNU version of awk, a versatile programming language for working on files. Related to: awk. |
| `_wk-GAWK` | GNU version of awk, a versatile programming language for working on files. Related to: awk.  More information: https://www.gnu.org/software/gawk/manual/gawk.html. |
| `_wk-gh` | gh is a CLI for GitHub. |
| `_wk-Gh` | gh is a Command Line Interface (CLI) which works seamlessly with GitHub. Some subcommands such as config have their own usage documentation. |
| `_wk-GH` | gh is a Command Line Interface (CLI) which works seamlessly with GitHub. Some subcommands such as config have their own usage documentation.  More information: https://cli.github.com/manual/gh. |
| `_wk-git` | git is a distributed version control software system. |
| `_wk-Git` | git is a distributed version control software system, that is capable of managing versions of source code or data.  More information: https://en.wikipedia.org/wiki/Git |
| `_wk-GIT` | git is a distributed version control software system, that is capable of managing versions of source code or data. It is often used to control source code by programmers who are developing software collaboratively.  More information: https://en.wikipedia.org/wiki/Git |
| `_wk-glab` | glab is a CLI for GitLab. |
| `_wk-Glab` | glab is a Command Line Interface (CLI) which works seamlessly with GitLab. Some subcommands such as config have their own usage documentation. |
| `_wk-GLAB` | glab is a Command Line Interface (CLI) which works seamlessly with GitLab. Some subcommands such as config have their own usage documentation.  More information: https://gitlab.com/gitlab-org/cli/-/tree/main/docs/source. |
| `_wk-grep` | grep can be used to find patterns in files using regexes. |
| `_wk-Grep` | grep is a CLI tool which can be used to find patterns in files using regexes (regular expressions). |
| `_wk-GREP` | grep is a CLI tool which can be used to find patterns in files using regexes (regular expressions).  More information: https://www.gnu.org/software/grep/manual/grep.html. |
| `_wk-gvim` | gvim is a Graphical User Interface version of Vim (Vi IMproved), a command-line text editor. |
| `_wk-Gvim` | gvim is a Graphical User Interface (GUI) version of Vim (Vi IMproved), a command-line text editor.  Related to: vimdiff, vimtutor, nvim, vim. |
| `_wk-GVIM` | gvim is a Graphical User Interface version of Vim (Vi IMproved), a command-line text editor.  Related to: vimdiff, vimtutor, nvim, vim. More information: https://www.vim.org. |
| `_wk-ls` | List directory contents (ls) |
| `_wk-Ls` | List directory contents.  More information: https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html. |
| `_wk-LS` | List directory contents.  More information: https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html. |
| `_wk-nvim` | Neovim is a programmer's text editor based on Vim. |
| `_wk-Nvim` | Neovim is a programmer's text editor based on Vim, which provides several modes for different kinds of text manipulation. |
| `_wk-NVIM` | Neovim is a programmer's text editor based on Vim, which provides several modes for different kinds of text manipulation.  Pressing <i> in normal mode enters insert mode. <Esc> or <Ctrl c> goes back to normal mode, which doesn't allow regular text insertion.  Related to: vim, vimtutor, vimdiff. More information: https://neovim.io. |
| `_wk-pwd` | Print the name of current/working directory (pwd). |
| `_wk-Pwd` | Print the name of current/working directory (pwd).  More information: https://www.gnu.org/software/coreutils/manual/html_node/pwd-invocation.html. |
| `_wk-PWD` | Print the name of current/working directory (pwd).  More information: https://www.gnu.org/software/coreutils/manual/html_node/pwd-invocation.html. |
| `_wk-rg` | ripgrep, a recursive line-oriented search tool. |
| `_wk-Rg` | ripgrep, a recursive line-oriented search tool. Aims to be a faster alternative to grep. |
| `_wk-RG` | ripgrep, a recursive line-oriented search tool. Aims to be a faster alternative to grep.  More information: https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md. |
| `_wk-ssh` | Secure Shell (SSH) |
| `_wk-Ssh` | Secure Shell (SSH) is a protocol used to securely log onto remote systems. It can be used for logging or executing commands on a remote server.. |
| `_wk-SSH` | Secure Shell is a protocol used to securely log onto remote systems. It can be used for logging or executing commands on a remote server.  More information: https://man.openbsd.org/ssh. |
| `_wk-svn` | Apache Subversion (abbreviated SVN, after its command name svn), is a version control system. |
| `_wk-Svn` | Apache Subversion (abbreviated SVN, after its command name svn), is a version control system.  Software developers use Subversion to maintain current and historical versions of files.  More information: https://en.wikipedia.org/wiki/Apache_Subversion |
| `_wk-SVN` | Apache Subversion (abbreviated SVN, after its command name svn), is a version control system distributed as open source under the Apache License.  Software developers use Subversion to maintain current and historical versions of files such as source code, web pages, and documentation.  More information: https://en.wikipedia.org/wiki/Apache_Subversion |
| `_wk-vdiff` | vimdiff opens up two or more files in vim and show the differences between them. |
| `_wk-Vdiff` | vimdiff open up two or more files in vim and show the differences between them. Related to: vim, vimtutor, nvim. |
| `_wk-VDIFF` | Open up two or more files in vim and show the differences between them. Related to: vim, vimtutor, nvim.  More information: https://www.vim.org. |
| `_wk-vim` | Vim (Vi IMproved) is a free and open-source, screen-based text editor program. It is an improved clone of Bill Joy's vi. |
| `_wk-Vim` | Vim (Vi IMproved) is a free and open-source, screen-based text editor program. It is an improved clone of Bill Joy's vi. Vim is designed for use both from a command-line interface and as a standalone application in a graphical user interface.  More information on: https://en.wikipedia.org/wiki/Vim_(text_editor) |
| `_wk-VIM` | Vim (Vi IMproved) is a free and open-source, screen-based text editor program. It is an improved clone of Bill Joy's vi. Vim is designed for use both from a command-line interface and as a standalone application in a graphical user interface.  More information on: https://en.wikipedia.org/wiki/Vim_(text_editor) |
| `_wk-vtutor` | vimtutor teaches the basic vim commands. |
| `_wk-Vtutor` | vimtutor teaches the basic vim commands. Related to: vim, vimdiff, nvim. |
| `_wk-VTUTOR` | vimtutor teaches the basic vim commands. Related to: vim, vimdiff, nvim.  More information: https://manned.org/vimtutor. |
