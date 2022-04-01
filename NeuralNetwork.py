"""
This file contains the NeuralNetwork class

Parameters:
    layers: list of integers, where the integers represent amount of nodes per layer

*Further explanation of class etc.*
*Also feel free to change the parameters if you think its better in some other way*

contributors: Mark Jacobsen, Will Gould, Abhinav Bhandari
"""
import numpy as np
import random

@np.vectorize
def sigmoid(x):
    """
    applies sigmoid function to all elements in np array
    :param x: the numpy array to apply sigmoid to
    :return: np array
    """
    return 1 / (1 + np.exp(-x))

class NeuralNetwork:
    def __init__(self, layers, activation=sigmoid):
        # setup
        self.layers = layers
        self.activation = activation

        # generate weights and biases
        # weights as list of two dimensional numpy arrays
        self.weights = [np.random.rand(layers[i + 1], layers[i]) for i in range(len(layers) - 1)]

        # biases as list of one dimensional numpy arrays
        self.biases = [np.random.rand(n, 1) for n in layers[1:]]

    def feed_forward(self, inputs):
        """
        feed through the network and generate outputs for specific inputs
        :param inputs: numpy array of values for the input layer nodes
        :return: 2D list of numpy arrays of values each representing the values in each layer
        """
        outputs = []
        for b, w in zip(self.biases, self.weights):
            inputs = np.dot(w, inputs) + b
            inputs = self.activation(inputs)
            outputs.append(inputs)
        return outputs

    def train(self, inputs, expected_outputs, learning_rate):
        """
        :param inputs: numpy array of values for the input layer nodes
        :param expected_outputs: numpy array of values that are what the output layer nodes should be
        :param learning_rate: how much the neural network changes its weights and biases in each training cycle
        """

        network_values = self.feed_forward(np.transpose(inputs))
        '''
        errors where [0] is output of the nn and [-1] is first hidden layer
        gradients where [0] is output of nn and [-1] is first hidden layer
        '''
        node_errors, node_gradients = self.backpropagation(network_values, expected_outputs)

        for i in range(0, len(node_errors) - 1):
            delta_bias = learning_rate * node_errors[i] * node_gradients[i]
            delta_weights = np.dot(delta_bias, np.transpose(network_values[-2 - i]))

            self.biases[-i - 1] = self.biases[-i - 1] + delta_bias
            self.weights[-i - 1] = self.weights[-i - 1] + delta_weights

        #last to change is the weights from the input nodes to the first hidden layer
        delta_bias = learning_rate * node_errors[-1] * node_gradients[-1]
        delta_weights = np.dot(delta_bias, inputs)

        self.biases[0] = self.biases[0] + delta_bias
        self.weights[0] = self.weights[0] + delta_weights  

    def backpropagation(self, network_values, expected_outputs):
        errors = [np.transpose(np.subtract(expected_outputs, np.transpose(network_values[-1])))]
        gradients = [[output * (1 - output) for output in network_values[-1]]]

        for i in range(len(network_values) - 1, 0, -1):
            errors.append(np.dot(np.transpose(self.weights[i]), errors[-1]))
            gradients.append([value * (1 - value) for value in network_values[i - 1]])


        return errors, gradients

    """
    other stuff...
    """

def main():
    network = NeuralNetwork([2, 2, 1])
    print(network.feed_forward(np.transpose(np.array([[0, 0]])))[-1])
    print(network.feed_forward(np.transpose(np.array([[1, 0]])))[-1])
    print(network.feed_forward(np.transpose(np.array([[0, 1]])))[-1])
    print(network.feed_forward(np.transpose(np.array([[1, 1]])))[-1])
    inputs = [[[[1, 0]], [1]], [[[0, 1]], [1]], [[[1, 1]], [1]], [[[0, 0]], [0]]]
    for i in range(0, 10000):
        test_data = random.choice(inputs)
        network.train(np.array(test_data[0]), np.array(test_data[1]), 0.1)
    print(network.feed_forward(np.transpose(np.array([[0, 0]])))[-1])
    print(network.feed_forward(np.transpose(np.array([[1, 0]])))[-1])
    print(network.feed_forward(np.transpose(np.array([[0, 1]])))[-1])
    print(network.feed_forward(np.transpose(np.array([[1, 1]])))[-1])

if __name__ == "__main__":
    main()
