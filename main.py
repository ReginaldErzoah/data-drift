import pygame
import sys

from game.player import Player
from game.enemy import DataEnemy
from game.score import Score
from game.background import Background
from game.juice import JuiceEngine
from game.visual_state import VisualState


# =========================
# INIT
# =========================
pygame.init()

WIDTH, HEIGHT = 800, 500

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Data Drift")
clock = pygame.time.Clock()


# =========================
# GAME OBJECTS
# =========================
player = Player()
enemies = []
score = Score()

bg = Background()
juice = JuiceEngine()
visual = VisualState()


# =========================
# HIGH SCORE
# =========================
high_score = 0


# =========================
# SPAWN SYSTEM (dynamic now)
# =========================
SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 900)


# =========================
# GAME STATE
# =========================
game_over = False
fullscreen = False


# =========================
# PHASE SYSTEM (NEW)
# =========================
def get_phase(score_value):

    if score_value < 20:
        return 1
    elif score_value < 50:
        return 2
    elif score_value < 100:
        return 3
    else:
        return 4


def get_speed_multiplier(phase):

    if phase == 1:
        return 1.0
    elif phase == 2:
        return 1.4
    elif phase == 3:
        return 1.8
    else:
        return 2.3


def get_spawn_rate(phase):

    if phase == 1:
        return 900
    elif phase == 2:
        return 750
    elif phase == 3:
        return 600
    else:
        return 450


# =========================
# RESTART
# =========================
def restart_game():
    global player, enemies, score, game_over

    player = Player()
    enemies.clear()
    score.reset()
    game_over = False

    visual.__init__()
    juice.reset()


# =========================
# MAIN LOOP
# =========================
while True:

    screen_width = screen.get_width()
    screen_height = screen.get_height()

    current_score = score.get_score()
    phase = get_phase(current_score)
    speed_multiplier = get_speed_multiplier(phase)

    # dynamically adjust spawn difficulty
    pygame.time.set_timer(SPAWN_EVENT, get_spawn_rate(phase))

    # =========================
    # UPDATE SYSTEMS
    # =========================
    juice.update()
    bg.update(screen_height, screen_width)
    visual.update(current_score, phase)

    # =========================
    # EVENTS
    # =========================
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # SPAWN
        if not game_over and event.type == SPAWN_EVENT:
            enemy = DataEnemy(screen_width)
            enemy.speed *= speed_multiplier
            enemies.append(enemy)

        # RESTART
        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()

        # FULLSCREEN
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:

                fullscreen = not fullscreen

                if fullscreen:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

    # =========================
    # SHAKE OFFSET
    # =========================
    shake_x, shake_y = juice.get_shake_offset()

    # =========================
    # FRAME BUFFER
    # =========================
    frame = pygame.Surface((screen_width, screen_height))
    frame.fill((10, 12, 20))

    # =========================
    # BACKGROUND
    # =========================
    bg.draw(frame)

    # =========================
    # GAMEPLAY
    # =========================
    if not game_over:

        player.update()

        for enemy in enemies[:]:
            enemy.update()
            enemy.speed_level = "CRITICAL" if phase >= 3 else "FAST" if phase == 2 else "NORMAL"

            if enemy.collides(player):
                game_over = True
                juice.trigger_hit()
                visual.trigger_hit()

            if enemy.y > screen_height:
                enemies.remove(enemy)
                score.add_survival()

        # DRAW ORDER
        for enemy in enemies:
            enemy.draw(frame)

        player.draw(frame)
        score.draw(frame)

    else:

        if score.get_score() > high_score:
            high_score = score.get_score()

        score.draw_final_score(frame)

        font = pygame.font.SysFont("Arial", 22)

        high_text = font.render(
            f"High Score: {high_score}",
            True,
            (255, 200, 100)
        )

        hint = font.render(
            "Press R to restart",
            True,
            (200, 200, 200)
        )

        frame.blit(high_text, (
            screen_width // 2 - high_text.get_width() // 2,
            300
        ))

        frame.blit(hint, (
            screen_width // 2 - hint.get_width() // 2,
            340
        ))

    # =========================
    # PRESENT FRAME
    # =========================
    screen.blit(frame, (shake_x, shake_y))

    juice.draw(screen)
    visual.draw(screen)

    pygame.display.update()
    clock.tick(60)