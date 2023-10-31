"""Implementation of the visualisation an interactive graph."""
from IPython.display import HTML, Javascript, display
from connectionz import DirectedGraph, UndirectedGraph, Node
from connectionz.draw_interactive.graph_processing import (
    graph_to_interactive_graph, interactive_graph_to_json, jsoned_graph_to_html
)
from connectionz.algorithms.connected_components.weakly_connected_components import search_weakly_connected_components

__all__ = ['draw_interactive']


def draw_interactive(
    graph: DirectedGraph | UndirectedGraph,
    window_height: int = 700,
    nodes_label: bool = True,
    nodes_label_align: str = 'bottom',
    nodes_positions: dict[Node, (float, float)] = None,
    nodes_colors: dict[Node, str] = None,
    nodes_sizes: dict[Node, int] = None
) -> None:
    """TODO"""
    interactive_graph = graph_to_interactive_graph(
        graph,
        groups_compile_algorithm=search_weakly_connected_components,
        nodes_label=nodes_label,
        nodes_label_align=nodes_label_align,
        nodes_positions=nodes_positions,
        nodes_colors=nodes_colors,
        nodes_sizes=nodes_sizes
    )
    jsoned_graph = interactive_graph_to_json(interactive_graph)
    html = jsoned_graph_to_html(jsoned_graph, window_height)
    # print(html)
    display(HTML(html))
