
#
# Implementing some functional patterns with ADTs
#
#
# Wishlist
#
# * Make match an expression. This would save having to repeat
#   a variable name when assigning.


from ast import Call
from dataclasses import dataclass
from typing import Any, TypeAlias, TypeVar, Generic, Callable
import datetime

from adt_1_order_status import OrderStatus_6, Ready, Scheduled, Shipped


# Result type

T = TypeVar("T")

@dataclass
class Ok(Generic[T]):
    value: T

    # def and_then(self, f: Callable[[T] -> Result[T]]) -> T:
    #     return f(self.value)

    def unwrap(self):
        return self.value

    def unwrap_or(self, _: T) -> T:
        return self.value

@dataclass
class Err:
    error: Any

    # def and_then(self, _: Any) -> "Err":
    #     return self

    def unwrap(self):
        raise Exception(self.error)

    def unwrap_or(self, default: Any) -> Any:
        return default


Result: TypeAlias = Ok[T] | Err


def order_date(status: OrderStatus_6) -> Result[datetime.date]:
    match (status):
        case Ready() | "unknown" | "not available":
            return Err("No date, unknown, or not available")

        case Scheduled(on) | Shipped(on):
            return Ok(on)


def time_since_order(status: OrderStatus_6) -> Result[datetime.timedelta]:
    match (order_date(status)):
        case Ok(date):
            return Ok(datetime.date.today() - date)

        case Err(error):
            return Err(error)


# def time_since_order_2(status: OrderStatus_6) -> Result:
#     return order_date(status).and_then(lambda date: Ok(datetime.date.today() - date))



if __name__ == "__main__":

    # Enforced error handling with Result
    match(order_date(Ready())):
        case Ok(date):
            print(f"Order date is {date}")
        case Err(error):
            print(f"Error: {error}")

    match(time_since_order(Ready())):
        case Ok(time_since):
            print(f"Time since order: {time_since}")
        case Err(error):
            print(f"Error: {error}")

    print("Time since order: ", time_since_order(Ready()))

    date = order_date(Ready())

    # Fails typecheck because the type checking points out that
    # Err doesn't have a `value` attribute.
    print(date.value)

    # Likewise, `date` may not have the error attribute; fails
    # typecheck.
    print(date.error)

    #
    # The type of `date` *must* be checked before accessing.
    # These succeed the typecheck because we handle the error case.
    #

    # Return the given default value on failure.
    print(date.unwrap_or(datetime.date.today()))

    # Crash the application on failure. Here, unwrap() = crash
    # because this is top-level code. It raises an Exception if
    # it's not `Ok(value)`.
    print(date.unwrap())

    # Pyright can't infer `date`'s type throught the `if`. 
    # This code doesn't typecheck.
    if date.is_ok():
        print(date.value)
    else:
        print(date.error)

    # Instead, we can use a match expression to handle the
    # error case. Pyright can do this flow analysis and type-narrowing.
    match (date):
        case Ok(date):
            print(date)
        case Err(error):
            print(error)

    
