from dataclasses import dataclass
import datetime
from enum import Enum
from typing import Any, Callable, Literal, TypeAlias

#
# Exhaustiveness checking an Enum
#


class OrderStatus(Enum):
    Ready = "ready"
    Scheduled = "scheduled"
    Shipped = "shipped"


def handle_order_1(status: OrderStatus) -> None:
    match (status):
        case OrderStatus.Ready:
            print("ship order")

        case OrderStatus.Shipped:
            print("change order")


def handle_order_2(status: OrderStatus) -> None:
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
def handle_order_3(status: OrderStatus) -> None:
    match (status):
        case OrderStatus.Ready:
            print("ship order")

        case OrderStatus.Scheduled:
            print("ship order")

        case OrderStatus.Shipped:
            print("change order")


#
# Exhaustiveness checking a Union
#


def get_float_1(num: str | float) -> float:
    match (num):
        case str(num):
            return float(num)


def get_float_2(num: str | float) -> float:
    match (num):
        case str(num):
            return float(num)

        case float(num):
            return num


#
# Exhaustiveness checking a Literal
#


Color = Literal["R", "G", "B"]


def get_color_name_1(color: Color) -> str:
    match (color):
        case "R":
            return "Red"

        case "G":
            return "Green"


def get_color_name_2(color: Color) -> str:
    match (color):
        case "R":
            return "Red"

        case "G":
            return "Green"

        case "B":
            return "Blue"


#
# Making an ADT with Python 10.
#


# Each status is now its own type with whatever attributes
# make sense for it.


@dataclass
class Ready:
    order_id: int


@dataclass
class Scheduled:
    on: datetime.date


@dataclass
class Shipped:
    on: datetime.date
    with_carrier: Literal["UPS", "Fedex", "USPS", "DHL"]


# Implicit TypeAlias, recognized by Pyright.
# This can also be written explicitly as:
#
# OrderStatus_5: TypeAlias = Ready | Scheduled | Shipped
OrderStatus_5 = Ready | Scheduled | Shipped


def handle_order_5(status: OrderStatus_5) -> None:
    match (status):
        case Ready(order_id):
            print(f"order #{order_id} is ready")

        case Scheduled(on) | Shipped(on):
            print(f"shipping date is {on}")


OrderStatus_6 = Literal["unknown"] | Ready | Scheduled | Shipped


def handle_order_6a(status: OrderStatus_6) -> None:
    match (status):
        case Ready(order_id):
            print(f"order #{order_id} is ready")

        case Scheduled(on) | Shipped(on):
            print(f"shipping date is {on}")


def handle_order_6b(status: OrderStatus_6) -> None:
    match (status):
        case Ready(order_id):
            print(f"order #{order_id} is ready")

        case Scheduled(on) | Shipped(on, with_carrier=_):
            print(f"shipping date is {on}")

        case "unknown":
            pass


handle_order_6b(Ready(order_id=110009))
handle_order_6b(Scheduled(on=datetime.date(2020, 1, 1)))
handle_order_6b(Shipped(on=datetime.date(2020, 1, 1), with_carrier="UPS"))
handle_order_6b("unknown")
handle_order_6b("unknwn")


#
# Implementing some functional patterns with ADTs
#


@dataclass
class Nothing:
    pass


@dataclass
class Just:
    value: Any


Maybe: TypeAlias = Just | Nothing

maybe: Callable[[Any], Maybe] = lambda x: Just(x) if x is not None else Nothing()


def order_date(status: OrderStatus_6) -> Maybe:
    ...


#
# Wishlist
#
# * Make match an expression. This would save having to repeat a variable name when assigning.
