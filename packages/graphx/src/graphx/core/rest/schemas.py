from marshmallow import Schema, fields


class Node(Schema):
    """Node schema"""
    id = fields.String(required=False)
    name = fields.String(required=False)


