import json
import logging
from dataclasses import dataclass

import falcon
from injector import inject

from graphx.core.data_providers.memory import Node
from graphx.core.exceptions import EntityAlreadyExistsException
from graphx.core.rest.schemas import Node as NodeSchema
from graphx.core.use_cases import AddNode


class NodeCollection(object):
    schema = NodeSchema()

    def __init__(self, add_node_usecase: AddNode):
        self.add_node = add_node_usecase

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




