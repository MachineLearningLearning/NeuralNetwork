"""
This file contains the Visualizer class

The Visualizer class is used to visualize a NeuralNetwork object.
It uses pygame for the graphics.
This file is mainly for the pygame setup and to link everything together.

Parameters:
    network: the NeuralNetwork object to visualize

contributors: Mark Jacobsen, *add your name here...*
"""
import pygame
pygame.init()
import NetworkVisualizer
import numpy as np
import time


class Visualizer:
    def __init__(self, network):
        # pygame setup
        self.screen = pygame.display.set_mode([800, 800])
        self.running = False
        self.clock = pygame.time.Clock()
        # other setup
        self.network = network
        self.network_visualizer = NetworkVisualizer.NetworkVisualizer(network, self.screen)
        self.fun = lambda: False

    def run(self):
        """
        main loop for running the visualization
        """
        self.running = True
        while self.running:
            # pygame stuff
            self.clock.tick(30)
            self.handle_events()
            # user defined function
            self.fun()
            # draw
            self.draw()

    def draw(self):
        """
        draw objects to pygame window
        """
        # background
        self.screen.fill((255, 255, 255))
        # network
        self.network_visualizer.draw()
        # flip display
        pygame.display.flip()

    def handle_events(self):
        """
        handle all pygame events
        """
        for event in pygame.event.get():
            # window close
            if event.type == pygame.QUIT:
                self.running = False
    

# test
if __name__ == "__main__":
    class nn:
        def __init__(self, layers) -> None:
            self.layers = layers
            # weights as list of two dimensional numpy arrays
            self.weights = self.generate_weights()

            # biases as list of one dimensional numpy arrays
            self.biases = [np.random.rand(n, 1) for n in layers[1:]]

        def generate_weights(self):
            return [np.random.rand(self.layers[i + 1], self.layers[i]) for i in range(len(self.layers) - 1)]

    network = nn([5, 2, 2, 1])
    vis = Visualizer(network)

    def fun():
        network.weights = network.generate_weights()
        vis.network_visualizer.reset()

    vis.fun = fun
    vis.run()