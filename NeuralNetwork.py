"""
This file contains the NeuralNetwork class

Parameters:
    layers: list of integers, where the integers represent amount of nodes per layer

*Further explanation of class etc.*
*Also feel free to change the parameters if you think its better in some other way*

contributors: Mark Jacobsen, Will Gould, *add your name here...*
"""
from distutils.log import error
import numpy as np
import random

class NeuralNetwork:
    def __init__(self, layers):
        # setup
        self.layers = layers

        # generate weights and biases
        # weights as list of two dimensional numpy arrays
        self.weights = [np.random.rand(layers[i + 1], layers[i]) for i in range(len(layers) - 1)]

        # biases as list of one dimensional numpy arrays
        self.biases = [np.random.rand(n, 1) for n in layers[1:]]


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
        feed through the network and generate outputs for specific inputs
        currently uses only the sigmoid activation function
        :param inputs: numpy array of values for the input layer nodes
        :return: 2D list of numpy arrays of values each representing the values in each layer
        """
        outputs = []
        for b, w in zip(self.biases, self.weights):
            inputs = np.dot(w, inputs) + b
            inputs = self.sigmoid(inputs)
            outputs.append(inputs)
        return outputs

    def train(self, inputs, expected_ouputs, learning_rate):
        """
        :param inputs: numpy array of values for the input layer nodes
        :param expected_outputs: numpy array of values that are what the output layer nodes should be
        :param learning_rate: how much the neural network changes its weights and biases in each training cycle
        """

        network_values = self.feed_forward(np.transpose(inputs))

        network_outputs = network_values[-1]
        output_errors = np.transpose(expected_ouputs) - network_outputs
        output_gradients = [output * (1 - output) for output in network_outputs]

        output_delta_bias = learning_rate * output_errors * output_gradients
        self.biases[-1] = np.add(self.biases[-1], output_delta_bias)

        errors = [output_errors]
        gradients = [output_gradients]

        for i in range(len(network_values) - 2, -1, -1):
            print(i)
            layer_values = network_values[i]
            layer_errors = np.dot(np.transpose(self.weights[i + 1]), errors[-1])
            layer_gradients = [value * (1 - value) for value in layer_values]
            print(errors[-1])
            print(layer_gradients)
            delta_biases = learning_rate * errors[-1] * layer_gradients #gradients[-1]
            delta_weights = np.dot(delta_biases, np.transpose(layer_values))

            self.weights[i + 1] = np.add(self.weights[i + 1], delta_weights)
            self.biases[i] = np.add(self.biases[i], delta_biases)

            errors.append(layer_errors)
            gradients.append(layer_gradients)
        print("out")

        '''
        hidden_values = network_values[0]
        hidden_errors = np.dot(np.transpose(self.weights[-1]), output_errors)
        hidden_gradients = [hidden_value * (1 - hidden_value) for hidden_value in hidden_values]

        delta_hidden_biases = learning_rate * np.dot(output_errors, output_gradients)
        delta_start_biases = learning_rate * hidden_errors * hidden_gradients

        #np.transpose(outputs) or np.transpose(hidden_layer_values)
        delta_hidden = np.dot(delta_hidden_biases, np.transpose(network_outputs))
        
        delta_start = np.dot(delta_start_biases, np.transpose(hidden_values))
        '''

        delta_start_biases = learning_rate * errors[-1] * gradients[-1]
        delta_start = np.dot(delta_start_biases, np.transpose(network_values[0]))
        self.weights[0] = np.add(self.weights[0], delta_start)

        #apply changes
        #print(self.weights)
        #self.weights[1] = np.add(self.weights[1], delta_hidden)
        #self.biases[1] = np.add(self.biases[1], delta_hidden_biases)

        
        

    def backpropagation(self):
        # someone claim this??
        return

    """
    other stuff...
    """

if __name__ == "__main__":
    network = NeuralNetwork([2, 2, 3, 1])
    print(network.feed_forward(np.transpose(np.array([[0, 0]])))[-1])
    print(network.feed_forward(np.transpose(np.array([[1, 0]])))[-1])
    print(network.feed_forward(np.transpose(np.array([[0, 1]])))[-1])
    print(network.feed_forward(np.transpose(np.array([[1, 1]])))[-1])
    print()
    inputs = [[[[1, 0]], [1]], [[[0, 1]], [1]], [[[1, 1]], [1]], [[[0, 0]], [0]]]
    for i in range(0, 1):
        test_data = inputs[random.randint(0, 3)]
        network.train(np.array(test_data[0]), np.array(test_data[1]), 0.1)
    print(network.feed_forward(np.transpose(np.array([[0, 0]])))[-1])
    print(network.feed_forward(np.transpose(np.array([[1, 0]])))[-1])
    print(network.feed_forward(np.transpose(np.array([[0, 1]])))[-1])
    print(network.feed_forward(np.transpose(np.array([[1, 1]])))[-1])