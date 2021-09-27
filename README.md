<h1><u>Gendiff:</u></h1>

<h3>Hexlet tests and linter status:</h3>
[![Actions Status](https://github.com/Tragoedie/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/Tragoedie/python-project-lvl2/actions)
[![check](https://github.com/Tragoedie/python-project-lvl2/actions/workflows/linter_test_check.yml/badge.svg)](https://github.com/Tragoedie/python-project-lvl2/actions/workflows/linter_test_check.yml)
<a href="https://codeclimate.com/github/Tragoedie/python-project-lvl2/maintainability"><img src="https://api.codeclimate.com/v1/badges/84ac06e864db4dcae66f/maintainability" /></a>
<a href="https://codeclimate.com/github/Tragoedie/python-project-lvl2/test_coverage"><img src="https://api.codeclimate.com/v1/badges/84ac06e864db4dcae66f/test_coverage" /></a>

<h1>Description:</h1>

Gendiff (GENerator of DIFFerences) is a program that detects the difference between two data structures (JSON or YAML) and generates a new structure containing details of the differences in different formats.

<h3>Supported formats:</h3> 
```bash
- 'stylish' output (--format stylish).

- 'plain' text output (--format plain).

- 'json' output (--format json).
```
<h2>Installation:</h2>

Use the package manager pip to install gendiff:
```bash
  pip install --user git+https://github.com/Tragoedie/python-project-lvl2.git
```

<h3>Optional arguments:</h3>
```bash
  -f, --format [type]  Output format: 'plain', 'json' or (default: 'stylish')
  -h, --help           output usage information
```
<h3>Positional arguments:</h3>
```bash
  first_file - path to the first file.
  second_file - path to the second file.
```
<h2>How use gendiff:</h2>

```bash
  $ gendiff [-f] file1 file2
```
<h3>'stylish' output format:</h3>
<a href="https://asciinema.org/a/f9CFp5SatZ8mYKCysUZVSeK8u" target="_blank"><img src="https://asciinema.org/a/f9CFp5SatZ8mYKCysUZVSeK8u.svg" /></a>
<h3>'plain' output format:</h3>
<a href="https://asciinema.org/a/sEVBnv1zLBZfcHW7uu124gF2y" target="_blank"><img src="https://asciinema.org/a/sEVBnv1zLBZfcHW7uu124gF2y.svg" /></a>
<h3>'json' output format:</h3>
<a href="https://asciinema.org/a/pocYGBjopEjdZQ6BkJwrTl88N" target="_blank"><img src="https://asciinema.org/a/pocYGBjopEjdZQ6BkJwrTl88N.svg" /></a>