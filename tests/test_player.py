import pygame
from game.player import Player

pygame.init()

def test_player_movement_bounds():
    player = Player()

    player.x = -100
    player.update()
    assert player.x >= 0

    player.x = 9999
    player.update()
    assert player.x <= 800  # default window assumption


def test_player_death_state():
    player = Player()
    player.die()

    assert player.is_dead == True