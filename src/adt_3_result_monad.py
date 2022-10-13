
#
# Implementing some functional patterns with ADTs
# This example makes Result into a Monad: it prevents
# direct access to its wrapped value.
#


from dataclasses import dataclass
from typing import Any, TypeAlias


# Result type, now as a Monad. (I think! It pretty much follows
# the Monad pattern.)


@dataclass(frozen=True)
class Ok:
    __value: Any  # Private for extra Monad-style safety

    def unwrap(self):
        return self.__value

    def unwrap_or(self, _: Any) -> Any:
        return self.__value

@dataclass(frozen=True)
class Err:
    __error: Any  # Private for extra Monad-style safety

    def unwrap(self):
        raise Exception(self.__error)

    def unwrap_or(self, default: Any) -> Any:
        return default


Result: TypeAlias = Ok | Err



if __name__ == "__main__":
    #
    # Demonstrating extra safety from the private attributes.
    #
    result = Ok(100)

    # Fails typecheck
    print(result.value)

    # Fails typecheck
    print(result.__value)

    # Passes typecheck: Can only get the inner value when we
    # handle the error case.
    value = result.unwrap_or(default=0)
