"""
This file contains the NetworkVisualizer class

The NetworkVisualizer class is used to visualize a NeuralNetwork object.
It uses pygame for the graphics.

Parameters:
    network: the NeuralNetwork object to visualize
    screen: pygame screen to draw on

contributors: Mark Jacobsen, *add your name here...*
"""
import Node


class NetworkVisualizer:
    def __init__(self, network, screen):
        self.network = network
        self.screen = screen
        self.node_radius = 20
        self.nodes = self.create_nodes()

    def create_nodes(self):
        """
        create the nodes to draw based on the network structure
        uses Node objects from Node.py file
        :return: list of lists for each layer in network
        """
        # get correct positions
        width, height = self.screen.get_size()
        y_distance = height / max(self.network.layers)
        x_distance = width / len(self.network.layers)

        # create nodes
        nodes = []
        current_x = x_distance / 2
        for layer in self.network.layers:
            current_y = (height - (layer - 1) * y_distance) / 2
            node_layer = []
            for _ in range(layer):
                n = Node.Node(current_x, current_y, self.node_radius, self.screen)
                node_layer.append(n)
                current_y += y_distance
            nodes.append(node_layer)
            current_x += x_distance
        return nodes

    def draw(self):
        """
        draw the network on the pygame screen
        :param screen: the pygame screen to draw on
        :return: None
        """
        # draw the nodes
        for layer in self.nodes:
            for n in layer:
                n.draw()