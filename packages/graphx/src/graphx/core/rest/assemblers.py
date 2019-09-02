from typing import List

from graphx.core.entities import Node
from graphx.core.rest.schemas import Node as NodeResource


class NodeAssembler(object):
    @staticmethod
    def assemble_collection(nodes: List[Node]) -> List[NodeResource]:
        return [NodeResource.from_domain_object(node) for node in nodes]
