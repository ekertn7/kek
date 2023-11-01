"""TODO"""
import os
import json
import sys
import uuid
import random
import warnings
from typing import Callable
from connectionz import DirectedGraph, UndirectedGraph, Node
from connectionz.exceptions.wrong_input_type import WrongInputTypeException
from connectionz.draw_interactive.interactive_graph import (
    IG_Info, IG_Node, IG_Edge, InteractiveGraph
)

__all__ = [
    'graph_to_interactive_graph',
    'interactive_graph_to_json',
    'jsoned_graph_to_html'
]


def _hexgen() -> str:
    return \
        f'#{"".join([random.choice("0123456789ABCDE") for _ in range(0, 6)])}'


def _make_groups(graph: DirectedGraph | UndirectedGraph, algorithm) \
        -> dict[Node, str]:
    """TODO"""
    groups = {}
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        warnings.warn('deprecated', DeprecationWarning)
        subgraphs = algorithm(graph)

    for i, subgraph in enumerate(subgraphs, 1):
        for node in subgraph.nodes.keys():
            groups[node] = f'Группа {i}'
    return groups


def _get_groups_info(groups: dict[Node, str]) -> list[dict[str, str]]:
    """TODO"""
    groups_info = []
    colors_hex = ['#FF0000', '#00FF00', '#0000FF', '#FF7F00', '#FFFF00',
                  '#2E2B5F', '#8B00FF', '#FF6600', '#FF9999', '#669933']
    groups_unique = list(set([v for v in groups.values()]))

    for group in groups_unique:
        if len(colors_hex) != 0:
            color = colors_hex[0]
            colors_hex.remove(color)
        else:
            color = _hexgen()
        groups_info.append({'group_name': group, 'group_color_hex': color})
    return groups_info


def _get_graph_layout(graph: DirectedGraph | UndirectedGraph) -> str:
    return 'Random'


def _is_graph_directed(graph: DirectedGraph | UndirectedGraph) -> bool:
    """TODO"""
    if not isinstance(graph, (DirectedGraph, UndirectedGraph)):
        raise WrongInputTypeException()
    if isinstance(graph, DirectedGraph):
        return True
    return False


def _make_ig_nodes(
        graph: DirectedGraph | UndirectedGraph,
        groups: dict[Node, str],
        groups_info: list[dict[str, str]],
        nodes_positions: dict[Node, (float, float)],
        nodes_colors: dict[Node, str],
        nodes_sizes: dict[Node, int]
) -> list[IG_Node]:
    result = []
    for node_name, node_attributes in graph.nodes.items():
        try:
            group_name = groups[node_name]
        except KeyError:
            group_name = None
        border_hex = '#000000'
        if group_name:
            border_hex = [
                gr['group_color_hex'] for gr in groups_info
                if gr['group_name'] == group_name
            ][0]
        result.append(
            IG_Node(
                node_name=node_name,
                node_attributes=node_attributes,
                shape='Circle',
                color_hex=nodes_colors[node_name] if nodes_colors else _hexgen(),
                border_hex=border_hex,
                group_name=group_name,
                position={
                    'x': nodes_positions[node_name][0] if nodes_positions
                         else random.randint(30, 700),
                    'y': nodes_positions[node_name][1] if nodes_positions
                         else random.randint(30, 600)
                },
                size=nodes_sizes[node_name] if nodes_sizes else 20
            )
        )
    return result


def _make_ig_edges(graph: DirectedGraph | UndirectedGraph) -> list[IG_Edge]:
    """TODO"""
    result = []
    for (node_left, node_right), edge_attributes in graph.edges.items():
        result.append(
            IG_Edge(
                edge_name=uuid.uuid4().hex,
                node_left=node_left,
                node_right=node_right,
                edge_attributes=edge_attributes,
                arrow_style='Line',
                line_style='Default',
                color_hex='#000000'
            )
        )
    return result


def graph_to_interactive_graph(
    graph: DirectedGraph | UndirectedGraph,
    groups_compile_algorithm: Callable,
    nodes_label: bool,
    nodes_label_align: str,
    nodes_positions: dict[Node, (float, float)],
    nodes_colors: dict[Node, str],
    nodes_sizes: dict[Node, int],
    show_nodes_without_groups: bool
) -> InteractiveGraph:
    """TODO"""
    groups = _make_groups(graph, algorithm=groups_compile_algorithm)
    groups_info = _get_groups_info(groups)
    return InteractiveGraph(
        IG_Info(
            directed=_is_graph_directed(graph),
            layout=_get_graph_layout(graph),
            groups=groups_info,
            nodes_label=nodes_label,
            nodes_label_align=nodes_label_align,
            show_nodes_without_groups=show_nodes_without_groups
        ),
        _make_ig_nodes(
            graph=graph,
            groups=groups,
            groups_info=groups_info,
            nodes_positions=nodes_positions,
            nodes_colors=nodes_colors,
            nodes_sizes=nodes_sizes
        ),
        _make_ig_edges(
            graph=graph
        )
    )


def interactive_graph_to_json(graph: InteractiveGraph) -> str:
    """TODO"""
    return json.dumps(graph.to_dict())


def jsoned_graph_to_html(
    graph: str,
    window_height: int
) -> str:
    """TODO"""
    frontend_folder = os.path.join(
        sys.path[1], 'connectionz', 'draw_interactive', 'frontend'
    )
    with open(
        os.path.join(frontend_folder, 'index.html'), 'r', encoding='utf-8'
    ) as template:
        html_template = template.read()
    with open(
        os.path.join(frontend_folder, 'js', 'code.js'), 'r', encoding='utf-8'
    ) as script_file:
        code = script_file.read()
    return html_template.format(
        graph_data=graph,
        code=code,
        window_height=window_height
    )
