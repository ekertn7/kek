"""Implementation of undirected graph."""
from connectionz import Node, Edge, Graph
from connectionz.exceptions.wrong_input_type import WrongInputTypeException

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

    def get_neighbors(self, selected_node: Node) -> list[Node]:
        """
        Get nodes connected to selected node.

        Arguments:
            selected_node: Selected node.

        Returns:
            List with neighbors of selected node.

        Example of usage:
            G.get_neighbors('A')
        """
        if not isinstance(selected_node, Node):
            raise WrongInputTypeException(selected_node, Node)
        neighbors = []
        for (node_l, node_r) in self.edges:
            if node_l == selected_node and node_r not in neighbors:
                neighbors.append(node_r)
            if node_r == selected_node and node_l not in neighbors:
                neighbors.append(node_l)
        return neighbors
