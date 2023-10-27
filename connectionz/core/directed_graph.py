"""Implementation of directed graph."""
from connectionz.core import Node, Edge, Graph

__all__ = ['DirectedGraph']


class DirectedGraph(Graph):
    """TODO"""
    def __str__(self):
        """Get graph type and information about count of nodes and edges."""
        return f'Directed graph wiht {len(self.nodes)} nodes and ' \
               f'{len(self.edges)} edges.'

    def __repr__(self) -> str:
        """Get two lists with nodes and edges."""
        return f'Directed graph wiht nodes: {self.nodes} and edges: ' \
               f'{self.edges}.'
