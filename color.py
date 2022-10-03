from enum import Enum


class Color(Enum):
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"  # I just added this


def handle_color(color: Color) -> None:
    match (color):
        case Color.RED:
            ...
        case Color.GREEN:
            ...
