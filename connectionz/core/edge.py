"""Base class to represent connection between two nodes."""
from typing import NamedTuple, Mapping, Any
from connectionz.core.node import Node

__all__ = ['Edge']


class Edge(NamedTuple):
    """Base class to represent connection between two nodes."""
    node_l: Node
    node_r: Node
    attributes: Mapping[str, Any] = None
