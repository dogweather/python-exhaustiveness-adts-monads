
#
# Implementing some functional patterns with ADTs
#
#
# Wishlist
#
# * Make match an expression. This would save having to repeat
#   a variable name when assigning.



from dataclasses import dataclass
import datetime
from typing import Any, Callable, TypeAlias

from order_status_adt import OrderStatus_6, Ready, Scheduled, Shipped


@dataclass
class Nothing:
    pass


@dataclass
class Just:
    value: Any


Maybe: TypeAlias = Just | Nothing

maybe: Callable[[Any], Maybe] = lambda x: Just(x) if x is not None else Nothing()


def order_date(status: OrderStatus_6) -> Maybe:
    match (status):
        case Ready() | "unknown" | "not available":
            return Nothing()

        case Scheduled(on) | Shipped(on):
            return Just(on)



if __name__ == "__main__":
    print(order_date(Ready()))
    print(order_date(Scheduled(datetime.date(2021, 1, 1))))
