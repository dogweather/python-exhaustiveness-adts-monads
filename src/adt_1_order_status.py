from dataclasses import dataclass
import datetime
from typing import Literal


#
# Making an Algebraic Data Type (ADT) with Python 10 + Pyright.
#


# Each status is now its own type with whatever attributes
# make sense for it.


@dataclass
class Ready:
    pass

@dataclass
class Scheduled:
    on: datetime.date


@dataclass
class Shipped:
    on: datetime.date
    with_carrier: Literal["UPS", "Fedex", "USPS", "DHL"]


OrderStatus_5 = Ready | Scheduled | Shipped


def handle_order_5(status: OrderStatus_5) -> None:
    match (status):
        case Ready():
            print("The order is ready")

        case Scheduled(on) | Shipped(on):
            print(f"Shipping date is {on}")



OrderStatus_6 = Literal["unknown", "not available"] | Ready | Scheduled | Shipped


#
# Fails typecheck: Literals "unknown" and "not available" are not
# handled.
#
def handle_order_6a(status: OrderStatus_6):
    match (status):
        case Ready():
            print("The order is ready")

        case Scheduled(on) | Shipped(on, with_carrier=_):
            print(f"shipping date is {on}")


#
# Passes typecheck.
#
def handle_order_6b(status: OrderStatus_6):
    match (status):
        case Ready():
            print("The order is ready")

        case Scheduled(on) | Shipped(on, with_carrier=_):
            print(f"shipping date is {on}")

        case "unknown":
            print("The order status hasn't been entered into the system yet")

        case "not available":
            print("System error: unable to access the order status")


if __name__ == "__main__":
    #
    # These all pass typecheck.
    #
    handle_order_6b(Ready())
    handle_order_6b(Scheduled(on=datetime.date(2020, 1, 1)))
    handle_order_6b(Shipped(on=datetime.date(2020, 1, 1), with_carrier="UPS"))
    handle_order_6b("unknown")

    # This typo is caught by Pyright: It fails the typecheck.
    # I.e., typos have been elevated to the type system, and are
    # caught at develop / CI time.
    handle_order_6b("unknwn")
