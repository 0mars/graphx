from typing import Any

from py2neo import Graph
from injector import inject
from dataclasses import dataclass

from graphx.core.data_provider import DataProvider, N
from graphx.core.entities import Node


@inject
@dataclass
class NodeRepository(DataProvider[Node]):
    graph: Graph

    def save(self, node: Node) -> None:
        self.graph.merge(node)

    def add_edge(self, source: Node, destination: Node) -> None:
        pass

    def find_by_id(self, id: str) -> Node:
        pass

    def find_shortest_path(self, source: N, destination: N) -> Any:
        pass
