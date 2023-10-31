"""Algorithm to get subgraph from a graph object."""
from typing import Iterable
from connectionz import DirectedGraph, UndirectedGraph, Node
from connectionz import WrongInputTypeException

__all__ = ['get_subgraph']


def get_subgraph(
        graph: DirectedGraph | UndirectedGraph,
    selected_nodes: Iterable[Node]
) -> DirectedGraph | UndirectedGraph:
    """
    Algorithm to get subgraph from a graph object.

    Arguments:
        graph:          A Graph object.
        selected_nodes: Iterable object with nodes that user wants to see
                        in subgraph.

    Returns:
        A Graph object.

    Example of usage:
        get_subgraph(graph, ['A', 'B', 'C', 'D'])
    """
    if isinstance(graph, UndirectedGraph):
        subgraph = UndirectedGraph()
    elif isinstance(graph, DirectedGraph):
        subgraph = DirectedGraph()
    else:
        raise WrongInputTypeException(graph, DirectedGraph, UndirectedGraph)
    for (node_l, node_r), edge_kwargs in graph.edges.items():
        if (node_l in selected_nodes) and (node_r in selected_nodes):
            subgraph.add_node(
                node_l, **graph.nodes[node_l], replace_existing=True
            )
            subgraph.add_node(
                node_r, **graph.nodes[node_r], replace_existing=True
            )
            subgraph.add_edge(
                node_l, node_r, **edge_kwargs, replace_existing=True
            )
    return subgraph
