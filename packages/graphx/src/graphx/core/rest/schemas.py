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



