#
# Exhaustiveness checking a Literal
#

from typing import Literal


Color = Literal["R", "G", "B"]


def get_color_name_1(color: Color):
    """
    Error raised:
        Unhandled type: "Literal['B']"
    """
    match (color):
        case "R":
            return "Red"

        case "G":
            return "Green"


def get_color_name_2(color: Color):
    """
    No error raised.
    """
    match (color):
        case "R":
            return "Red"

        case "G":
            return "Green"

        case "B":
            return "Blue"
