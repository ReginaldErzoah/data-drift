import pygame
import sys
import random

from game.player import Player
from game.enemy import DataEnemy
from game.score import Score

pygame.init()

WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Data Drift")

clock = pygame.time.Clock()

player = Player()
enemies = []
score = Score()

SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 900)

game_over = False
speed_boost = 0

while True:

    screen.fill((10, 12, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not game_over and event.type == SPAWN_EVENT:
            enemy = DataEnemy()
            enemy.speed += speed_boost
            enemies.append(enemy)

        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                enemies.clear()
                player = Player()
                score = Score()
                game_over = False
                speed_boost = 0

    if not game_over:

        player.update()

        for enemy in enemies[:]:
            enemy.update()
            enemy.draw(screen)

            if enemy.collides(player):
                game_over = True

            if enemy.y > HEIGHT:
                enemies.remove(enemy)
                score.add_survival()

        # difficulty scaling
        if pygame.time.get_ticks() % 2500 < 16:
            speed_boost += 0.5

        player.draw(screen)
        score.draw(screen)

    else:
        font = pygame.font.SysFont("Arial", 40)
        text = font.render("DATA DRIFT CORRUPTED", True, (255, 80, 80))
        screen.blit(text, (170, 200))

        sub = pygame.font.SysFont("Arial", 20)
        hint = sub.render("Press R to restart", True, (200, 200, 200))
        screen.blit(hint, (300, 260))

    pygame.display.update()
    clock.tick(60)