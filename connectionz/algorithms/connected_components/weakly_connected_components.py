from connectionz import DirectedGraph, UndirectedGraph
from connectionz import WrongInputTypeException
from connectionz.algorithms.breadth_first_search.breadth_first_search import breadth_first_search
from connectionz.algorithms.subgraph.subgraph import get_subgraph

__all__ = [
    'search_weakly_connected_components'
]


def search_weakly_connected_components(graph: DirectedGraph | UndirectedGraph) -> list:
    """TODO"""
    visited_nodes = []
    result = []
    if isinstance(graph, DirectedGraph):
        graph = UndirectedGraph(graph.nodes, graph.edges)
        for node in graph.nodes:
            if node not in visited_nodes:
                connected_nodes = list(breadth_first_search(graph, node))
                connected_nodes.append(node)
                visited_nodes.extend(connected_nodes)
                output_graph = DirectedGraph(graph.nodes, graph.edges)
                result.append(get_subgraph(output_graph, connected_nodes))
    elif isinstance(graph, UndirectedGraph):
        for node in graph.nodes:
            if node not in visited_nodes:
                connected_nodes = list(breadth_first_search(graph, node))
                connected_nodes.append(node)
                visited_nodes.extend(connected_nodes)
                result.append(get_subgraph(graph, connected_nodes))
    else:
        raise WrongInputTypeException()
    return result
