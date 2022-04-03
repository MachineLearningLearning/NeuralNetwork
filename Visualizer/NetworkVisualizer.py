"""
This file contains the NetworkVisualizer class

The NetworkVisualizer class is used to visualize a NeuralNetwork object.
It uses pygame for the graphics.

Parameters:
    network: the NeuralNetwork object to visualize
    screen: pygame screen to draw on

contributors: Mark Jacobsen, *add your name here...*
"""
from .Node import Node
from .Weight import Weight


class NetworkVisualizer:
    def __init__(self, network, screen):
        self.network = network
        self.screen = screen
        self.node_radius = 20
        self.nodes = self.create_nodes()
        self.weights = self.create_weights()

    def reset(self):
        """
        reset after weight change etc.
        """
        # reset weights
        new_weights = []
        for c, layer in enumerate(self.nodes[:-1]):
            new_weight_layer = []
            # loop through nodes of current layer
            for c2 in range(len(layer)):
                # loop through nodes in next layer
                for c3 in range(len(self.nodes[c + 1])):
                    new_weight_layer.append(round(self.network.weights[c][c3][c2], 2))
            new_weights.append(new_weight_layer)
        for l in range(len(new_weights)):
            for w in range(len(new_weights[l])):
                self.weights[l][w].weight = new_weights[l][w] 

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
                n = Node(current_x, current_y, self.node_radius, self.screen)
                node_layer.append(n)
                current_y += y_distance
            nodes.append(node_layer)
            current_x += x_distance
        return nodes

    def create_weights(self):
        """
        creates the weights of the network by considering the nodes
        """
        weights = []
        for c, layer in enumerate(self.nodes[:-1]):
            weight_layer = []
            # loop through nodes of current layer
            for c2, node in enumerate(layer):
                # loop through nodes in next layer
                for c3, node2 in enumerate(self.nodes[c + 1]):
                    weight = Weight(node, node2, self.screen)
                    weight.weight = round(self.network.weights[c][c3][c2], 2)
                    weight_layer.append(weight)
            weights.append(weight_layer)
        return weights

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
        # draw the weights
        for weight_layer in self.weights:
            for weight in weight_layer:
                weight.draw()