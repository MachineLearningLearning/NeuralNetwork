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


class Visualizer:
    def __init__(self, network):
        # pygame setup
        self.screen = pygame.display.set_mode([800, 800])
        self.running = False
        self.clock = pygame.time.Clock()
        # other setup
        self.network = network
        self.network_visualizer = NetworkVisualizer.NetworkVisualizer(network, self.screen)

    def run(self):
        """
        main loop for running the visualization
        """
        self.running = True
        while self.running:
            self.clock.tick(30)
            self.handle_events()
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
    vis = Visualizer(nn([5, 2, 2, 1]))
    vis.run()