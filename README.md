# Python Exhaustiveness Checking Demo

Demo code showing off the new true exhaustiveness checks with Python 3.10 + Pyright.
I created this repo to support my blog post and make it easy to try out
this technique.

## To set up

You'll need [Poetry](https://python-poetry.org) and Python 3.10. I used 3.10.6 and 3.10.7 to write this.

```
poetry install
poetry shell
```

## Now you can run Pyright

To see the exhaustiveness checks for all the files:

```
pyright
```

## VS Code

VS Code has **Pylance** checking built into its Python extension. This
brings the Pyright checking into the IDE. IMO it's an amazing experience.

Pylance/Pyright should pick up
the settings from `pyproject.toml`. The settings in VS Code seem to mostly
be overridden by the file.
