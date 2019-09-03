import logging
from dataclasses import dataclass, field
from typing import Any, List, Dict

from graphx.core.data_providers.data_provider import DataProvider
from graphx.core.entities import Edge, Node
from graphx.core.exceptions import EntityAlreadyExistsException

@dataclass
class MemoryNodeRepository(DataProvider[Node, Edge]):
    nodes: Dict[str, Node] = field(default_factory=lambda: {})
    edges: List[Edge] = field(default_factory=lambda: [])

    def save(self, node: Node) -> None:
        if node.id in self.nodes:
            raise EntityAlreadyExistsException('Node already exists!')
        self.nodes[node.id] = node

    def add_edge(self, edge: Edge) -> None:
        # todo handle duplicates
        self.edges.append(edge)

    def find_all_nodes(self) -> List[Node]:
        return [v for k, v in self.nodes.items()]

    def find_by_id(self, id: str) -> Node:
        pass

    def find_shortest_path(self, source: Node, destination: Node) -> Any:
        pass
