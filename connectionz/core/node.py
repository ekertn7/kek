"""Base class to represent a node."""
from typing import TypeAlias, Union

__all__ = ['Node']


Node: TypeAlias = Union[str, int, float]
