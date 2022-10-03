# Originally "4 - Exhaustiveness checking with mypy"
# by Daily dose of Python.
# https://jerry-git.github.io/daily-dose-of-python/doses/4/

# Modified to use the new exhaustiveness checking enabled
# by Python 3.10's match statement and Pyright's MatchNotExhaustive
# check.

from enum import Enum


class Color(Enum):
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"  # I just added this


# Reports MatchNotExhaustive:
#   Unhandled type: "Literal[Color.BLUE]"
def handle_color(color: Color) -> None:
    match (color):
        case Color.RED:
            ...
        case Color.GREEN:
            ...