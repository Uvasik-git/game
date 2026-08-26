import pygame

from player import Player
from enemy import Enemy

pygame.init()

screen = pygame.display.set_mode((800, 600))
players = [Player(100, 200), Enemy(500, 300)]
# player_1 = players[0]
# enemy_1 = players[1]
clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    dt = clock.tick(60) / 1000

    screen.fill((23, 45, 68))

    for sprite in players:
        sprite.update(keys, dt)

    if players[0].rect.colliderect(players[1].rect):
        players[0].health -= 10
        print("Boom")

    for sprite in players:
        sprite.draw(screen)

    pygame.display.flip()

pygame.quit()
