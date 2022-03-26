"""
This file contains the NetworkVisualizer class

The NetworkVisualizer class is used to visualize a NeuralNetwork object.
It uses pygame for the graphics.

Parameters:
    network: the NeuralNetwork object to visualize

contributors: Mark Jacobsen, *add your name here...*
"""
import Node


class NetworkVisualizer:
    def __init__(self, network):
        self.network = network
        self.nodes = self.create_nodes()

    def create_nodes(self):
        """
        create the nodes to draw based on the network structure
        uses Node objects from Node.py file
        :return: list of lists for each layer in network
        """
        nodes = []
        for layer in self.network.layer:
            node_layer = []
            for _ in range(layer):
                n = Node(10, 10, 10)
                node_layer.append(n)
            nodes.append(node_layer)
        return nodes

    def draw(self, screen):
        """
        draw the network on the pygame screen
        :param screen: the pygame screen to draw on
        :return: None
        """
        # draw the nodes
        for layer in self.nodes:
            for n in layer:
                n.draw(screen)