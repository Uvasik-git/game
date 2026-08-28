import pygame

from player import Player
from enemy import Enemy

pygame.init()

screen = pygame.display.set_mode((800, 600))
players = [Player(100, 200), Enemy(500, 300)]
# player_1 = players[0]
# enemy_1 = players[1]
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

running = True
game_over = False
last_damage_time = 0

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    dt = clock.tick(60) / 1000
    current_time = pygame.time.get_ticks()
    screen.fill((23, 45, 68))

    if not game_over:
        for sprite in players:
            sprite.update(keys, dt)

        if players[0].rect.colliderect(players[1].rect) and current_time - last_damage_time >= 1000:
            players[0].health -= 10
            last_damage_time = current_time
            print("Boom")

        if players[0].health <= 0:
            game_over = True

    for sprite in players:
        sprite.draw(screen)

    health_text = font.render(f"Здоровье: {players[0].health}", True, (255, 255, 255))
    screen.blit(health_text, (20, 20))

    pygame.display.flip()

pygame.quit()
