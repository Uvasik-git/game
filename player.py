import pygame

from game_object import GameObject

class Player(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = (36, 60, 130)
        self.speed = 300

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def update(self, keys, dt):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed * dt
            if self.rect.left < 0:
                self.rect.left = 0
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed * dt
            if self.rect.right > 800:
                self.rect.right = 800
        elif keys[pygame.K_UP]:
            self.rect.y -= self.speed * dt
            if self.rect.top < 0:
                self.rect.top = 0
        elif keys[pygame.K_DOWN]:
            self.rect.y += self.speed * dt
            if self.rect.bottom > 600:
                self.rect.bottom = 600

