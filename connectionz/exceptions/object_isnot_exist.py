"""Exception class when an object that is not exists is called."""
from typing import Optional

__all__ = ['ObjectIsNotExistException']


class ObjectIsNotExistException(Exception):
    """Exception class when an object that is not exists is called."""
    def __init__(self, object_name: Optional[str] = None):
        self.message = \
            f'This {object_name if object_name else "object"} is not exist!'

    def __str__(self):
        return self.message
