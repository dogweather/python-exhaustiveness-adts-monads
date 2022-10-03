#
# Exhaustiveness checking a Union type
#


# Reports MatchNotExhaustive:
#     Unhandled type: "float"
#
# Also reports GeneralTypeIssues:
#     Function with declared type of "float" must return value
#     Type "None" cannot be assigned to type "float"
def get_float_1(num: str | float) -> float:
    match (num):
        case str(num):
            return float(num)


# No error reported.
def get_float_2(num: str | float) -> float:
    match (num):
        case str(num):
            return float(num)

        case float(num):
            return num
