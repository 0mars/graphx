from dataclasses import dataclass

from injector import inject

from graphx.core.data_providers.memory import MemoryNodeRepository
from graphx.core.entities import Edge


@inject
@dataclass
class AddEdge:
    repository: MemoryNodeRepository

    def execute(self, edge: Edge):
        # todo assert nodes exist before adding
        self.repository.add_edge(edge)
