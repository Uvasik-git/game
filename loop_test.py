import main
running = True
t = 0
while running:

    t += 1
    main.screen
    print(t)

import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))

print(type(screen))

print(help(pygame))