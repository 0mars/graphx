from marshmallow import Schema, fields

from graphx.core.entities import Node as DomainNode


class Node(Schema):
    """Node schema"""
    id = fields.String(required=False)
    name = fields.String(required=False)

    @classmethod
    def from_domain_object(cls, node: DomainNode):
        object = cls()
        object.id = node.id
        object.name = node.name
        return object


class Edge(Schema):
    """Edge schema"""
    source = fields.String()
    destination = fields.String()
    cost = fields.Integer()

    @classmethod
    def from_domain_object(cls, edge):
        object = cls()
        object.source = edge.source
        object.destination = edge.destination
        object.cost = edge.cost
        return object
