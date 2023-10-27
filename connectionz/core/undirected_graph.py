"""Implementation of undirected graph."""
from connectionz.core import Node, Edge, Graph

__all__ = ['UndirectedGraph']


class UndirectedGraph(Graph):
    """TODO"""
    def __str__(self):
        """Get graph type and information about count of nodes and edges."""
        return f'Undirected graph wiht {len(self.nodes)} nodes and ' \
               f'{len(self.edges)} edges.'

    def __repr__(self) -> str:
        """Get two lists with nodes and edges."""
        return f'Undirected graph wiht nodes: {self.nodes} and edges: ' \
               f'{self.edges}.'
