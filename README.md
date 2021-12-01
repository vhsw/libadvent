# libadvent

Helper library for [Advent of Code](https://adventofcode.com) :christmas_tree:

## Usage

Install the package with:

```console
poetry install
```

Set `SESSION` env var to your session cookie from [Advent of Code](https://adventofcode.com).
`.env` file is also supported.

`download` will scrape your puzzle input and create a template file for answers.
Example:

```console
download 2020-12-25
```

Without args, `download` will scrape puzzle input for today.

`update_stats` will update the amounts of sweet shiny stars :star: that you earned in your readme file.
