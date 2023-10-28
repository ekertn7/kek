"""TODO"""
from typing import Any
from dataclasses import dataclass

__all__ = ['InteractiveGraph', 'IG_Info', 'IG_Node', 'IG_Edge']


@dataclass
class IG_Info:
    """TODO"""
    directed: bool
    layout: str
    groups: list[dict[str, str]]

    def to_dict(self) -> dict:
        """TODO"""
        return self.__dict__


@dataclass
class IG_Node:
    """TODO"""
    node_name: str
    node_attributes: dict[str, Any]
    shape: str
    color_hex: str
    border_hex: str
    group_name: str
    position: dict[str, float]
    size: int

    def to_dict(self) -> dict:
        """TODO"""
        return self.__dict__


@dataclass
class IG_Edge:
    """TODO"""
    edge_name: str
    node_left: str
    node_right: str
    edge_attributes: dict[str, Any]
    arrow_style: str
    line_style: str
    color_hex: str

    def to_dict(self) -> dict:
        """TODO"""
        return self.__dict__


@dataclass
class InteractiveGraph:
    """TODO"""
    info: IG_Info
    nodes: list[IG_Node]
    edges: list[IG_Edge]

    def to_dict(self) -> dict:
        return {
            'info': self.info.to_dict(),
            'nodes': [node.to_dict() for node in self.nodes],
            'edges': [edge.to_dict() for edge in self.edges]
        }
