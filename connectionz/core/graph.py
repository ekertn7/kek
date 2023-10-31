"""Base class to represent any graph."""
from uuid import uuid4
from typing import Union, Mapping, Iterable, Any
from abc import ABC, abstractmethod
from connectionz import Node, Edge
from connectionz.exceptions.wrong_input_type import WrongInputTypeException
from connectionz.exceptions.object_already_exist import ObjectAlreadyExistException

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

    def add_node(self, node: Node, replace_existing: bool = False, **kwargs) \
        -> None:
        """
        Add a new node to a graph.

        Arguments:
            node:             Unique node name.
            replace_existing: True = existing node will be replaced by new.
                              False = existing node will NOT be replaced by new.
            kwargs:           Node attributes.

        Examples:
            G.add_node('A')
            G.add_node('B', name='Nikita', age=25)
        """
        if not isinstance(node, Node):
            raise WrongInputTypeException(node, Node)
        if replace_existing:
            self.nodes[node] = kwargs
        else:
            if node not in self.nodes:
                self.nodes[node] = kwargs
            else:
                raise ObjectAlreadyExistException(object_name='node')

    def add_edge(self, node_l: Node, node_r: Node,
                 replace_existing: bool = False, **kwargs) -> None:
        """
        Add a new directed edge to a graph.

        Arguments:
            node_l:           Node that affects the second node.
            node_r:           Node that affected by the first node.
            replace_existing: True = existing edge will be replaced by new.
                              False = existing edge will NOT be replaced by new.
            kwargs:           Edge attributes.

        Examples:
            G.add_edge('A', 'B')
            G.add_edge('C', 'D', weight=1.23, label='sale')
        """
        if not isinstance(node_l, Node):
            raise WrongInputTypeException(node_l, Node)
        if not isinstance(node_r, Node):
            raise WrongInputTypeException(node_r, Node)
        if replace_existing:
            self.edges[Edge(node_l, node_r)] = kwargs
        else:
            if (node_l, node_r) not in self.edges:
                self.edges[Edge(node_l, node_r)] = kwargs
            else:
                raise ObjectAlreadyExistException(object_name='edge')

    @abstractmethod
    def get_neighbors(self, selected_node: Node) -> list[Node]:
        """Get nodes connected to selected node."""
