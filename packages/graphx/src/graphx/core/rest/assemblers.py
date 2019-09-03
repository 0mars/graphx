from typing import List

from graphx.core.entities import Node, Edge
from graphx.core.rest.schemas import Node as NodeResource
from graphx.core.rest.schemas import Edge as EdgeResource


class NodeAssembler(object):
    @staticmethod
    def assemble_collection(nodes: List[Node]) -> List[NodeResource]:
        return [NodeResource.from_domain_object(node) for node in nodes]


class EdgeAssembler(object):
    @staticmethod
    def assemble_collection(edges: List[Edge]) -> List[EdgeResource]:
        return [EdgeResource.from_domain_object(edge) for edge in edges]
