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
# SPAWN SYSTEM
# =========================
SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 900)


# =========================
# GAME STATE
# =========================
game_over = False
speed_boost = 0
fullscreen = False


# =========================
# SPEED LEVEL (READABILITY SIGNAL)
# =========================
def get_speed_level():
    if speed_boost < 5:
        return "NORMAL"
    elif speed_boost < 12:
        return "FAST"
    return "CRITICAL"


# =========================
# RESTART
# =========================
def restart_game():
    global player, enemies, score, game_over, speed_boost

    player = Player()
    enemies.clear()
    score.reset()
    game_over = False
    speed_boost = 0

    # reset visual systems only
    visual.__init__()
    juice.reset()


# =========================
# MAIN LOOP
# =========================
while True:

    screen_width, screen_height = screen.get_size()

    speed_level = get_speed_level()

    # =========================
    # UPDATE SYSTEMS
    # =========================
    juice.update()
    bg.update(screen_height, screen_width)
    visual.update(score.get_score(), speed_boost)

    # =========================
    # EVENTS
    # =========================
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
                restart_game()

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
    # BACKGROUND LAYER
    # =========================
    bg.draw(frame)

    # =========================
    # GAMEPLAY
    # =========================
    if not game_over:

        player.update()

        for enemy in enemies[:]:
            enemy.update()
            enemy.speed_level = speed_level

            if enemy.collides(player):
                game_over = True
                juice.trigger_hit()
                visual.trigger_hit()

            if enemy.y > screen_height:
                enemies.remove(enemy)
                score.add_survival()

        # difficulty scaling
        if pygame.time.get_ticks() % 2500 < 16:
            speed_boost += 0.5

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