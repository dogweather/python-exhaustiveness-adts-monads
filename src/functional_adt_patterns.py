
#
# Implementing some functional patterns with ADTs
#
#
# Wishlist
#
# * Make match an expression. This would save having to repeat
#   a variable name when assigning.



from dataclasses import dataclass
from typing import Any, Callable, TypeAlias
import datetime

from order_status_adt import OrderStatus_6, Ready, Scheduled, Shipped


#
# Dynamically typed Maybe
#

@dataclass
class Nothing:
    pass

@dataclass
class Just:
    value: Any


Maybe: TypeAlias = Just | Nothing



def order_date(status: OrderStatus_6) -> Maybe:
    match (status):
        case Ready() | "unknown" | "not available":
            return Nothing()

        case Scheduled(on) | Shipped(on):
            return Just(on)


# Idea: Maybe constructor. Wraps a value in a Maybe.
#       Not used in this example.
# maybe: Callable[[Any], Maybe] = lambda x: Just(x) if x is not None else Nothing()


# Result type

@dataclass
class Ok:
    value: Any

    def unwrap(self):
        return self.value

@dataclass
class Err:
    error: Any

    def unwrap(self):
        raise Exception(self.error)


Result: TypeAlias = Ok | Err


def order_date_2(status: OrderStatus_6) -> Result:
    match (status):
        case Ready() | "unknown" | "not available":
            return Err("No date, unknown, or not available")

        case Scheduled(on) | Shipped(on):
            return Ok(on)


def time_since_order(status: OrderStatus_6) -> Result:
    match (order_date_2(status)):
        case Ok(date):
            return Ok(datetime.date.today() - date)

        case Err(error):
            return Err(error)


def time_since_order_2(status: OrderStatus_6) -> datetime.timedelta:
   return datetime.date.today() - order_date_2(status).unwrap()



if __name__ == "__main__":

    # Enforced error handling with Maybe
    match (order_date(Ready())):
        case Just(date):
            print(f"Order date is {date}")
        case Nothing():
            print("No order date")

    # Enforced error handling with Result
    match(order_date_2(Ready())):
        case Ok(date):
            print(f"Order date is {date}")
        case Err(error):
            print(f"Error: {error}")

    match(time_since_order(Ready())):
        case Ok(time_since):
            print(f"Time since order: {time_since}")
        case Err(error):
            print(f"Error: {error}")

    print("Time since order: ", time_since_order_2(Ready()))
