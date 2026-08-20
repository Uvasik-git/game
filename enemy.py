import pygame

from game_object import GameObject

class Enemy(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = (200, 50, 50)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, 25)

    def update(self, kyes, dt):
        pass