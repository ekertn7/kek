"""Exception class when an object that already exists is called."""
from typing import Optional


class ObjectAlreadyExistException(Exception):
    """Exception class when an object that already exists is called."""
    def __init__(self, object_name: Optional[str] = None):
        self.message = \
            f'This {object_name if object_name else "object"} already exist! ' \
            f'If you want to replace this ' \
            f'{object_name if object_name else "object"} by new, please ' \
            f'change attribute replace_existing in current method to True.'

    def __str__(self):
        return self.message
