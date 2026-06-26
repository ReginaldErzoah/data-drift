import pygame

from game.player import Player
from game.enemy import DataEnemy
from game.score import Score
from game.background import Background
from game.visual_state import VisualState

pygame.init()

def test_basic_initialization():
    player = Player()
    enemy = DataEnemy(800)
    score = Score()
    bg = Background()
    visual = VisualState()

    assert player is not None
    assert enemy is not None
    assert score.get_score() == 0
    assert bg is not None
    assert visual is not None