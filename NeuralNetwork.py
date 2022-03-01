"""
This file contains the NeuralNetwork class

Parameters:
    layers: list of integers, where the integers represent amount of nodes per layer

*Further explanation of class etc.*
*Also feel free to change the parameters if you think its better in some other way*

contributors: Mark Jacobsen, *add your name here...*
"""
import numpy as np


class NeuralNetwork:
    def __init__(self, layers):
        # setup
        self.layers = layers

        # generate weights and biases
        # weights as list of two dimensional numpy arrays
        self.weights = []
        # biases as list of one dimensional numpy arrays
        self.biases = []

    @staticmethod
    def sigmoid(arr):
        """
        applies sigmoid function to all elements in np array
        :param arr: the numpy array to apply sigmoid to
        :return: np array
        """
        sigm = lambda x: 1 / (1 + np.exp(-x))
        npfunc = np.vectorize(sigm)
        return npfunc(arr)

    def feed_forward(self, inputs):
        """
        feed through the network and generate outputs
        for specific inputs
        :param inputs: numpy array of values for the input layer nodes
        :return: list of values each representing one output from an output node
        """
        for b, w in zip(self.biases, self.weights):
            inputs = np.dot(w, inputs) + b
            inputs = self.sigmoid(inputs)
        return inputs

    def train(self, inputs, expected_ouputs):
        # someone claim this??
        return

    def backpropagation(self):
        # someone claim this??
        return

    """
    other stuff...
    """