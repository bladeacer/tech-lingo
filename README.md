## tech-lingo

An Espanso package with terms commonly used in the tech sector. WIP.

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
Descriptions and definitions were taken from:
- [Wikipedia](https://www.wikipedia.org/)
- [tldr pages](https://github.com/tldr-pages/tldr)

We thank the contributors of these projects for their excellent work.

---

## License
This Espanso package, "tech-lingo", is a collection of code and content under different licenses.

### For the Espanso Package Code and Original Rules
The configuration files and original Espanso rules in this package are licensed under the **GNU General Public License version 3 (GPLv3)**. You can find the full license text in the [LICENSE.GPL](LICENSE.GPL) file.

### For All Sourced Content
The descriptions and definitions from **Wikipedia** and **tldr pages** are licensed under the **Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)**. You can find the full license text in the [LICENSE.CC-BY-SA](LICENSE.CC-BY-SA) file.

---

### License Notices
You should have received a copy of the licenses along with this project.
If not, you can find them in the repository's root directory.
