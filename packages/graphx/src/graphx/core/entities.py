from attr import dataclass


@dataclass
class Node:
    id: str
    name: str


@dataclass
class Edge:
    source: Node
    destination: Node
    cost: int
