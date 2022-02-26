"""
This file contains the NeuralNetwork class

Parameters:
    input_nodes: the amount of input nodes as integer
    middle_layers: list of integers, where the integers represent amount of nodes per layer
    output_nodes: the amount of output nodes

*Further explanation of class etc.*
*Also feel free to change the parameters if you think its better in some other way*

contributors: Mark Jacobsen, *add your name here...*
"""
import numpy as np


class NeuralNetwork:
    def __init__(self, input_nodes, middle_layers, output_nodes):
        self.input_nodes = input_nodes
        self.middle_layers = middle_layers
        self.output_nodes = output_nodes

    def feed_forward(self, inputs):
        """
        feed through the network and generate outputs
        for specific inputs
        :param inputs: list of values for the input layer nodes
        :return: list of values each representing one output from an output node
        """
        # I (Mark Jacobsen) will work on this...
        return

    def train(self, inputs, expected_ouputs):
        # someone claim this??
        return

    def backpropagation(self):
        # someone claim this??
        return

    """
    other stuff...
    """