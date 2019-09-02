from injector import Module, singleton, provider

from graphx.core.data_providers.memory import MemoryNodeRepository
from graphx.core.rest.resources import NodeCollection
from graphx.core.use_cases import AddNode


class NodeConfigurator(Module):
    @singleton
    @provider
    def node_collection(self) -> NodeCollection:
        return NodeCollection(self.__injector__.get(AddNode))

    @singleton
    @provider
    def repository(self) -> MemoryNodeRepository:
        return MemoryNodeRepository()
