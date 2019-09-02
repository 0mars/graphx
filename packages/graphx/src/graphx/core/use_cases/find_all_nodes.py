from dataclasses import dataclass
from typing import List

from injector import inject

from graphx.core.data_providers.memory import Node, MemoryNodeRepository


@inject
@dataclass
class FindAllNodes:
    repository: MemoryNodeRepository

    def execute(self) -> List[Node]:
        return self.repository.find_all_nodes()
