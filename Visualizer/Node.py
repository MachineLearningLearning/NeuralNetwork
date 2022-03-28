"""
This file contains the Node class

A node object represents a single node in a neural network.
This class is used to visualize that single node with pygame.

Parameters:
    x: x position for pygame to draw
    y: y position for pygame to draw
    radius: the size of the node
    screen: pygame screen to draw on

contributors: Mark Jacobsen, *add your name here...*
"""
import pygame


class Node:
    def __init__(self, x, y, radius, screen):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = (0, 0, 0)
        self.screen = screen

    def draw(self):
        """
        draw the node on the pygame screen
        :return: None
        """
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)