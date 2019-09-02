from py2neo.ogm import GraphObject, Property, RelatedTo
from typing import Any

from py2neo import Graph as NeoGraph
from injector import inject
from dataclasses import dataclass

from graphx.core.data_providers.data_provider import DataProvider


class Node(GraphObject):
    __primarykey__ = "id"

    id = Property()
    name = Property()

    edges = RelatedTo('Node')


@inject
@dataclass
class NeoNodeRepository(DataProvider[Node]):
    graph: NeoGraph

    def save(self, node: Node) -> None:
        self.graph.merge(node)

    def add_edge(self, source: Node, destination: Node, cost: int) -> None:
        pass

    def find_by_id(self, id: str) -> Node:
        pass

    def find_shortest_path(self, source: Node, destination: Node) -> Any:
        pass
