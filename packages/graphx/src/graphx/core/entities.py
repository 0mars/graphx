from dataclasses import dataclass


@dataclass
class Node:
    id: str
    name: str


@dataclass
class Edge:
    source: str
    destination: str
    cost: int
