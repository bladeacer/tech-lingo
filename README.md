## tech-lingo

An Espanso package with terms commonly used in the IT sector. WIP.

## Installation

Installation as an external package.
> Will add to Espanso Hub at some point

```
espanso install tech-lingo --git https://github.com/bladeacer/tech-lingo --external
```

## FAQ

### Why underscore as the trigger prefix?
`_` conflicts less than `:` or `/` especially in editors like Vim.

### Why are there multiple letter casings for the same snippet?

E.g. `_vim` returns
```
Vim (Vi IMproved)
```

`_Vim` returns
```
Vim (Vi IMproved), a command-line text editor,
provides several modes for different kinds of text manipulation.
```

`_VIM` returns
```
Vim (Vi IMproved), a command-line text editor,
provides several modes for different kinds of text manipulation.

More information: https://www.vim.org.
```

In short, casing is a way to indicate output verbosity.

There are some commands like `_Pwd` and `_PWD` with the same verbosity.

## Credits
Plenty of descriptions and definitions were taken from [tldr pages](https://github.com/tldr-pages/tldr).

## License
This Espanso package, "tech-lingo" is released under the GNU General Public
License version 3 (GPLv3) License.

### License Notice
```
This file is part of tech-lingo. tech-lingo is a CLI tool that lets you add
folders to backup manually to a target Git repository. 

Copyright (c) 2025 bladeacer

tech-lingo is free software: you can redistribute it and/or modify it under the
terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later version.

tech-lingo is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with tech-lingo.
If not, see <https://www.gnu.org/licenses/>. 
```
