#
# Exhaustiveness checking a Union type
#


def get_float_1(num: str | float) -> float:
    """
    Error raised:
        Unhandled type: "float"
    """
    match (num):
        case str(num):
            return float(num)


def get_float_2(num: str | float) -> float:
    """
    No error raised.
    """
    match (num):
        case str(num):
            return float(num)

        case float(num):
            return num
