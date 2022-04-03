"""
Module contains the Weight class for visualization purposes
"""
import pygame

class Weight:
    def __init__(self, Node1, Node2, screen):
        self.weight = 0
        self.Node1 = Node1
        self.Node2 = Node2
        self.color = (0, 0, 0)
        self.screen = screen

    def draw(self):
        """
        draw the weight on the pygame screen
        """
        pygame.draw.line(self.screen, self.color, (self.Node1.x, self.Node1.y), (self.Node2.x, self.Node2.y))