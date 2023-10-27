"""Implementation of the visualisation an interactive graph."""
import json
import os.path
from typing import Union
from IPython.display import HTML, display
from connectionz import DirectedGraph, UndirectedGraph

__all__ = ['draw_interactive']


def graph_to_interactive_graph(graph: DirectedGraph | UndirectedGraph):
    pass


def interactive_graph_to_json() -> str:
    return json.dumps({
        "info":
            {
                "directed": True,
                "layout": "Circle",
                "groups": [
                    {
                        "group_name": "Group_1",
                        "group_color": "#0000FF"
                    },
                    {
                        "group_name": "Group_2",
                        "group_color": "#FF0000"
                    }
                ]
            },
        "nodes":
            [
                {
                    "node_name": "n_1",
                    "node_attributes": {},
                    "shape": "Circle",
                    "color_hex": "#555555",
                    "border_hex": "#0000FF",
                    "group_name": "Group_1",
                    "position:": {"x": 80, "y": 140},
                    "size": 50
                },
                {
                    "node_name": "n_2",
                    "node_attributes": {},
                    "shape": "Circle",
                    "color_hex": "#777777",
                    "border_hex": "#FF0000",
                    "group_name": "Group_2",
                    "position:": {"x": 200, "y": 360},
                    "size": 50
                }
            ],
        "edges":
            [
                {
                    "edge_name": "e_1_2",
                    "node_left": "n_1",
                    "node_right": "n_2",
                    "edge_attributes": {},
                    "arrow_style": "triangle",
                    "line_style": "default",
                    "color_hex": "#000000"
                }
            ]
        })


def jsoned_graph_to_html(graph: str, window_height: int):
    """TODO"""
    frontend_folder = r'/Users/ekertn7/Desktop/Projects/ConnectionZ/' \
                      r'connectionz/draw_interactive/frontend'
    with open(
        os.path.join(frontend_folder, 'index.html'), 'r', encoding='utf-8'
    ) as template:
        html_template = template.read()
    with open(
        os.path.join(frontend_folder, 'js', 'code.js'), 'r', encoding='utf-8'
    ) as script_file:
        code = script_file.read()
    return html_template.format(graph_data=json.loads(graph), code=code, window_height=window_height)


def draw_interactive(
    graph: DirectedGraph | UndirectedGraph,
    window_height: int = 450
) -> None:
    """TODO"""
    # interactive_graph = graph_to_interactive_graph(graph)
    jsoned_graph = interactive_graph_to_json()
    html = jsoned_graph_to_html(jsoned_graph, window_height)
    # print(html)
    display(HTML(html))
