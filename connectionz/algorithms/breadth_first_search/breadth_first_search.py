from connectionz import DirectedGraph, UndirectedGraph, Node
from connectionz import ObjectIsNotExistException

__all__ = ['breadth_first_search']


def breadth_first_search(
    graph: DirectedGraph | UndirectedGraph,
    source_node: Node = None
):
    """TODO"""
    visited_nodes = set()
    if source_node not in graph.nodes:
        raise ObjectIsNotExistException()

    nodes_query = [source_node]
    while nodes_query:
        current_node = nodes_query[0]
        nodes_query.remove(current_node)
        if current_node not in visited_nodes:
            yield current_node
        visited_nodes.add(current_node)
        for neighbor in graph.get_neighbors(current_node):
            if neighbor not in visited_nodes:
                nodes_query.append(neighbor)
