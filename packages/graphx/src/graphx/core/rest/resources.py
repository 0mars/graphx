import json
import logging

import falcon

from graphx.core.data_providers.memory import Node
from graphx.core.entities import Edge
from graphx.core.exceptions import EntityAlreadyExistsException
from graphx.core.rest.assemblers import NodeAssembler, EdgeAssembler
from graphx.core.rest.schemas import Node as NodeSchema
from graphx.core.rest.schemas import Edge as EdgeSchema
from graphx.core.use_cases import AddNode
from graphx.core.use_cases.add_edge import AddEdge
from graphx.core.use_cases.find_all_edges import FindAllEdges
from graphx.core.use_cases.find_all_nodes import FindAllNodes


class NodeCollection(object):
    schema = NodeSchema()

    def __init__(self, add_node: AddNode, find_all_nodes: FindAllNodes):
        self.add_node = add_node
        self.find_all_nodes = find_all_nodes

    def on_post(self, req, resp):
        """
            ---
                           summary: Add a node
                           responses:
                               201:
                                   description: Created
                                   schema: Node
        """
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
        """
            ---
                           summary: Find all nodes
                           responses:
                               200:
                                   description: OK
        """
        nodes = self.find_all_nodes.execute()
        schema = NodeSchema(many=True)
        result = schema.dump(NodeAssembler.assemble_collection(nodes))  # OR UserSchema().dump(users, many=True)
        resp.body = json.dumps(result)

        resp.status = falcon.status_codes.HTTP_200


class EdgeCollection(object):
    schema = EdgeSchema()

    def __init__(self, add_edge: AddEdge, find_all_edges: FindAllEdges):
        self.add_use_case = add_edge
        self.find_all_use_case = find_all_edges

    def on_post(self, req, resp):
        """
            ---
                           summary: Add an edge
                           responses:
                               201:
                                   description: Created
                                   schema: Edge
        """
        edge_resource = req.context['json']

        edge = Edge(edge_resource['source'], edge_resource['destination'], edge_resource['cost'])
        try:
            self.add_use_case.execute(edge)
            resp.body = json.dumps(edge_resource)
            resp.status = falcon.status_codes.HTTP_201
        except EntityAlreadyExistsException:
            # todo response error body
            resp.status = falcon.status_codes.HTTP_422

    def on_get(self, req, resp):
        """
            ---
                           summary: Find all edges
                           responses:
                               200:
                                   description: OK
        """
        edges = self.find_all_use_case.execute()
        schema = EdgeSchema(many=True)
        result = schema.dump(EdgeAssembler.assemble_collection(edges))  # OR UserSchema().dump(users, many=True)
        resp.body = json.dumps(result)

        resp.status = falcon.status_codes.HTTP_200
