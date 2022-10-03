from enum import Enum

#
# Original Source: https://hakibenita.com/python-mypy-exhaustive-checking.
# It uses `assert_never` to simulate exhaustive checking.
#
# Python will introduce assert_never() in 3.11.
# https://typing.readthedocs.io/en/latest/source/unreachable.html
#

#
# Modified to play with the functions, and to use the new
# exhaustiveness checking enabled by Python 3.10's match statement
# and Pyright's MatchNotExhaustive check.
#


class OrderStatus(Enum):
    Ready = "ready"
    Scheduled = "scheduled"
    Shipped = "shipped"


# Reports MatchNotExhaustive:
#   Cases within match statement do not exhaustively handle all values.
#   Unhandled type: "Literal[OrderStatus.Scheduled]"
def handle_order_1(status: OrderStatus):
    match (status):
        case OrderStatus.Ready:
            print("ship order")

        case OrderStatus.Shipped:
            print("change order")


# Reports MatchNotExhaustive:
#   Cases within match statement do not exhaustively handle all values
#   Unhandled type: "Literal[OrderStatus.Scheduled]"
def handle_order_2(status: OrderStatus):
    match (status):
        case OrderStatus.Ready:
            print("ship order")

        case OrderStatus.Shipped:
            print("change order")

    raise ValueError(f"Status {status} is not valid")


# Fully exhaustive, with the benefits:
#
# * No Exceptions raised. (Fewer runtime errors.)
# * No default case needed. (A crutch for the lack of exhaustiveness checking.)
# * No need to check for unknown cases. (A crutch for the lack of exhaustiveness checking.)
# * Every case is handled, now and in the future.
# * The code is shorter and more expressive.
def handle_order_3(status: OrderStatus):
    match (status):
        case OrderStatus.Ready:
            print("ship order")

        case OrderStatus.Scheduled:
            print("ship order")

        case OrderStatus.Shipped:
            print("change order")
