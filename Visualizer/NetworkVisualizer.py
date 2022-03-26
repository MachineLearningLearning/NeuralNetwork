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
        # TODO need to do the x,y maths here for better visualization
        current_x = 100
        for layer in self.network.layers:
            current_y = 100
            node_layer = []
            for _ in range(layer):
                n = Node.Node(current_x, current_y, 20)
                node_layer.append(n)
                current_y += 100
            nodes.append(node_layer)
            current_x += 100
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