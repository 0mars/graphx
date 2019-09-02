from injector import Module, singleton, provider

from graphx.core.data_providers.memory import MemoryNodeRepository
from graphx.core.rest.resources import NodeCollection
from graphx.core.use_cases import AddNode
from graphx.core.use_cases.find_all_nodes import FindAllNodes


class NodeConfigurator(Module):
    @singleton
    @provider
    def node_collection(self) -> NodeCollection:
        return NodeCollection(self.__injector__.get(AddNode), self.__injector__.get(FindAllNodes))

    @singleton
    @provider
    def repository(self) -> MemoryNodeRepository:
        return MemoryNodeRepository()
