import pygame

class GameObject:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 80)

    def update(self, keys, dt):
        pass

    def draw(self, screen):
        pass