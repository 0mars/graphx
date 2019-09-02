import json
import logging

import falcon

from graphx.core.data_providers.memory import Node
from graphx.core.exceptions import EntityAlreadyExistsException
from graphx.core.rest.assemblers import NodeAssembler
from graphx.core.rest.schemas import Node as NodeSchema
from graphx.core.use_cases import AddNode
from graphx.core.use_cases.find_all_nodes import FindAllNodes


class NodeCollection(object):
    schema = NodeSchema()

    def __init__(self, add_node: AddNode, find_all_nodes: FindAllNodes):
        self.add_node = add_node
        self.find_all_nodes = find_all_nodes

    def on_post(self, req, resp):
        node_resource = req.context['json']

        node = Node(id=node_resource['id'], name=node_resource['name'])
        try:
            self.add_node.execute(node)
            resp.body = json.dumps(node_resource)
            resp.status = falcon.status_codes.HTTP_201
        except EntityAlreadyExistsException:
            # todo response error body
            resp.status = falcon.status_codes.HTTP_422

    def on_get(self, req, resp):
        nodes = self.find_all_nodes.execute()
        schema = NodeSchema(many=True)
        result = schema.dump(NodeAssembler.assemble_collection(nodes))  # OR UserSchema().dump(users, many=True)
        resp.body = json.dumps(result)

        resp.status = falcon.status_codes.HTTP_200
