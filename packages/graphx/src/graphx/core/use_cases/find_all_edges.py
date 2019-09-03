from dataclasses import dataclass
from typing import List

from injector import inject

from graphx.core.data_providers.memory import Edge, MemoryNodeRepository


@inject
@dataclass
class FindAllEdges:
    repository: MemoryNodeRepository

    def execute(self) -> List[Edge]:
        return self.repository.find_all_edges()
