# Originally from "4 - Exhaustiveness checking with mypy"
# by Daily dose of Python.
# https://jerry-git.github.io/daily-dose-of-python/doses/4/

# Modified to use the new true exhaustiveness checking enabled
# by Python 3.10's match statement and Pyright's MatchNotExhaustive
# check.

from enum import Enum


class Color(Enum):
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"  # I just added this


def handle_color(color: Color) -> None:
    """
    Error raised:
        Unhandled type: "Literal[Color.BLUE]"
    """
    match (color):
        case Color.RED:
            ...
        case Color.GREEN:
            ...
