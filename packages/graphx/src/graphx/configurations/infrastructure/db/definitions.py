from dataclasses import dataclass

from injector import Module, singleton, provider
from py2neo import Graph


@dataclass
class GraphConfigurator(Module):
    url: str
    username: str
    password: str

    @singleton
    @provider
    def provide_graph(self) -> Graph:
        # graph = Graph(uri=self.url, user=self.username, password=self.password)
        graph = Graph("http://neo4j:7474/db/data/", user=self.username, password=self.password)
        # graph.create()
        return graph.begin()
        # return graph
