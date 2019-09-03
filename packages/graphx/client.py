from collections import deque, namedtuple

# we'll use infinity as a default distance to nodes.
import requests

inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')


def make_edge(edge):
    return Edge(edge['source'], edge['destination'], edge['cost'])


class Graph:
    def __init__(self, edges):
        # let's check that the data is right
        self.edges = [make_edge(edge) for edge in edges]

    @property
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )

    def get_node_pairs(self, n1, n2):
        return [[n1, n2]]

    def remove_edge(self, n1, n2):
        node_pairs = self.get_node_pairs(n1, n2)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1):
        node_pairs = self.get_node_pairs(n1, n2)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours

    def dijkstra(self, source, dest):
        assert source in self.vertices, 'Such source node doesn\'t exist'
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == inf:
                break
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        return path


base_url = 'http://localhost:8021/v1'

edges = [
    {
        "source": "A",
        "destination": "B",
        "cost": 7
    },
    {
        "source": "A",
        "destination": "C",
        "cost": 9
    },
    {
        "source": "A",
        "destination": "F",
        "cost": 14
    },
    {
        "source": "B",
        "destination": "C",
        "cost": 10
    },
    {
        "source": "B",
        "destination": "D",
        "cost": 15
    },
    {
        "source": "C",
        "destination": "D",
        "cost": 11
    },
    {
        "source": "C",
        "destination": "F",
        "cost": 2
    },
    {
        "source": "D",
        "destination": "E",
        "cost": 6
    },
    {
        "source": "E",
        "destination": "F",
        "cost": 9
    }
]
for edge in edges:
    r = requests.post('{}/edges'.format(base_url), json=edge)

r = requests.get('{}/edges'.format(base_url))
response = r.json()
graph = Graph(response)

print("\npath: \n")
print(graph.dijkstra("A", "E"))
