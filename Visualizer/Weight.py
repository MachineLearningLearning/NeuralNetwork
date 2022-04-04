"""
Module contains the Weight class for visualization purposes
"""
import pygame

class Weight:
    def __init__(self, Node1, Node2, screen):
        self.weight = 0
        self.Node1 = Node1
        self.Node2 = Node2
        self.weight_pos = self.calculate_weight_pos()
        self.color = (0, 0, 0)
        self.font = pygame.font.SysFont('arial', 15)
        self.screen = screen

    def __repr__(self):
        return str(self.weight)

    def calculate_weight_pos(self):
        """
        calculate the position the weight value will be displayed at
        """
        dy = 1 if (self.Node2.y - self.Node1.y) == 0 else (self.Node2.y - self.Node1.y)
        dx = (self.Node2.x - self.Node1.x)
        slope = dy / dx
        f = lambda x: slope * x + self.Node1.y
        v = 50
        return (v + self.Node1.x, f(v))

    def draw(self):
        """
        draw the weight on the pygame screen
        """
        pygame.draw.line(self.screen, self.color, (self.Node1.x, self.Node1.y), (self.Node2.x, self.Node2.y))
        text = self.font.render(str(self.weight), True, self.color)
        self.screen.blit(text, self.weight_pos)