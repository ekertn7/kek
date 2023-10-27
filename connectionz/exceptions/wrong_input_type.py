"""Exception class when incorrect input type."""
from typing import Optional, Any


class WrongInputTypeException(Exception):
    """Exception class when incorrect input type."""
    def __init__(
        self,
        current_object: Optional[Any] = None,
        *expected_types: type
    ):
        if current_object and expected_types:
            self.message = \
                f'Expected ' \
                f'{"type" if len(expected_types) == 1 else "types"} ' \
                f'{", ".join([str(elem) for elem in expected_types])}, ' \
                f'got {type(current_object)} instead!'
        else:
            self.message = 'You are using an unsupported object type!'

    def __str__(self):
        return self.message
