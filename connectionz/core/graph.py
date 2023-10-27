"""Base class to represent any graph."""
from uuid import uuid4
from typing import Union, Mapping, Iterable, Any
from abc import ABC, abstractmethod
from connectionz.core import Node, Edge
from connectionz.exceptions import WrongInputTypeException

__all__ = ['Graph']


class Graph(ABC):
    """Base class to represent any graph."""
    def __init__(
        self,
        nodes: Union[
            Mapping[Node, Mapping[str, Any]],
            Iterable[Node]
        ] = None,
        edges: Union[
            Mapping[Edge, Mapping[str, Any]],
            Iterable[Edge]
        ] = None
    ):
        """
        Initialization.

        Arguments:
            nodes: Mapping or iterable object with nodes.
            edges: Mapping or iterable object with edges.

        Examples:
            1. Make graph with nodes and edges attributes.
            G = Graph(
                nodes={'A': {'name': 'Alexa'}, 'B': {'name': 'Boris'}},
                edges={Edge('A', 'B'): {'weight': 7}}
            )
            2. Make graph without nodes and edges attributes.
            G = Graph(
                nodes=['A', 'B'], edges=[Edge('A', 'B')]
            )
        """
        self.id = uuid4().hex

        if isinstance(nodes, Mapping):
            self.nodes = {node: attribute for node, attribute in nodes.items()}
        elif isinstance(nodes, Iterable):
            self.nodes = {node: {} for node in nodes}
        elif nodes is None:
            self.nodes = {}
        else:
            raise WrongInputTypeException(nodes, Mapping, Iterable)

        if isinstance(edges, Mapping):
            self.edges = {edge: attribute for edge, attribute in edges.items()}
        elif isinstance(edges, Iterable):
            self.edges = {edge: {} for edge in edges}
        elif edges is None:
            self.edges = {}
        else:
            raise WrongInputTypeException(edges, Mapping, Iterable)

    @abstractmethod
    def __str__(self):
        """Get graph type and information about count of nodes and edges."""

    @abstractmethod
    def __repr__(self) -> str:
        """Get two lists with nodes and edges."""

    def __len__(self):
        """Get the number of nodes in graph."""
        return len(self.nodes)

    def __eq__(self, other):
        """Get the result of comparison two graphs."""
        if isinstance(other, type(self)):
            return self.nodes == other.nodes and self.edges == other.edges
        else:
            raise WrongInputTypeException(other, Graph)
