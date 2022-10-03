#
# Exhaustiveness checking a Literal
#

from typing import Literal


Color = Literal["R", "G", "B"]


# Reports MatchNotExhaustive:
#   Cases within match statement do not exhaustively handle all values.
#   Unhandled type: "Literal['B']"
def get_color_name_1(color: Color):
    match (color):
        case "R":
            return "Red"

        case "G":
            return "Green"


# No error reported.
def get_color_name_2(color: Color):
    match (color):
        case "R":
            return "Red"

        case "G":
            return "Green"

        case "B":
            return "Blue"
