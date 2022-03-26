"""
This file contains the Visualizer class

The Visualizer class is used to visualize a NeuralNetwork object.
It uses pygame for the graphics.

Parameters:
    network: the NeuralNetwork object to visualize

contributors: Mark Jacobsen, *add your name here...*
"""
import pygame
pygame.init()


class Visualizer:
    def __init__(self, network):
        self.network = network
        # pygame setup
        self.screen = pygame.display.set_mode([800, 800])
        self.running = False

    def run(self):
        """
        main loop for running the visualization
        """
        self.running = True
        while self.running:
            self.handle_events()
            self.draw()

    def draw(self):
        """
        draw objects to pygame window
        """
        # background
        self.screen.fill((255, 255, 255))
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
    vis = Visualizer(None)
    vis.run()