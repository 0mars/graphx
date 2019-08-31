from py2neo.ogm import GraphObject, Property, RelatedTo


class Node(GraphObject):
    __primarykey__ = "id"

    id = Property()
    name = Property()

    edges = RelatedTo('Node')

