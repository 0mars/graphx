from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar, Any

N = TypeVar('N')
E = TypeVar('E')


class DataProvider(Generic[N, E], metaclass=ABCMeta):
    @abstractmethod
    def save(self, node: N) -> None:
        """ ads a node to the graph
                Args:
                    node (N): The node entity
                Returns:
                    None
        """
        pass

    @abstractmethod
    def add_edge(self, edge: E) -> None:
        """ ads an edge
                Args:
                    source: source node
                    destination: destination node
                    cost: cost of distance
                Returns:
                    None
                """
        pass

    @abstractmethod
    def find_by_id(self, id: str) -> N:
        """ finds a node by id
                Args:
                    id: Node id
                Returns:
                    N
                Raises:
                    EntityNotFoundException
        """
        pass

    @abstractmethod
    def find_shortest_path(self, source: N, destination: N) -> Any:
        """ finds the shortest path
                Args:
                    source: Source node
                    destination: Destination node
                Returns:
                    Any should be shortest path object
        """
