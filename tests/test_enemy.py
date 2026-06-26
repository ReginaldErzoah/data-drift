import pygame
from game.enemy import DataEnemy

pygame.init()

def test_enemy_spawns_within_screen():
    enemy = DataEnemy(800)

    assert 0 <= enemy.x <= 800


def test_enemy_movement():
    enemy = DataEnemy(800)

    start_y = enemy.y
    enemy.update()

    assert enemy.y > start_y