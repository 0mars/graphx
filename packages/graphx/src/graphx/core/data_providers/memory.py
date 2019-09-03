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
        if self.edge_exists(edge):
            raise EntityAlreadyExistsException('Edge already exists')
        self.edges.append(edge)

    def edge_exists(self, edge: Edge):
        # todo shall only compare source and dest
        duplicates = [existing_edge for existing_edge in self.edges if edge == existing_edge]
        return len(duplicates) > 0

    def find_all_nodes(self) -> List[Node]:
        return [v for k, v in self.nodes.items()]

    def find_by_id(self, id: str) -> Node:
        pass

    def find_all_edges(self) -> List[Edge]:
        return self.edges

    def find_shortest_path(self, source: Node, destination: Node) -> Any:
        pass
