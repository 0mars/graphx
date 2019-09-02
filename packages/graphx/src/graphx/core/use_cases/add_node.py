from dataclasses import dataclass

from injector import inject

from graphx.core.data_providers.memory import Node, MemoryNodeRepository


@inject
@dataclass
class AddNode:
    repository: MemoryNodeRepository

    def execute(self, node: Node):
        self.repository.save(node)
