"""
This file contains the Node class

A node object represents a single node in a neural network.
This class is used to visualize that single node with pygame.

Parameters:
    x: x position for pygame to draw
    y: y position for pygame to draw
    radius: the size of the node

contributors: Mark Jacobsen, *add your name here...*
"""
import pygame


class Node:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = (0, 0, 0)

    def draw(self, screen):
        """
        draw the node on the pygame screen
        :param screen: pygame screen to draw on
        :return: None
        """
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)