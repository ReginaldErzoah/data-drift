import pygame
import sys

from game.player import Player
from game.enemy import DataEnemy
from game.score import Score
from game.background import Background
from game.juice import JuiceEngine


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
# READABILITY / DIFFICULTY STATE (NEW)
# =========================
def get_speed_level():
    """
    Central readability signal.
    Used by enemies/player to simplify visuals at high speed.
    """
    if speed_boost < 5:
        return "NORMAL"
    elif speed_boost < 12:
        return "FAST"
    else:
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


# =========================
# MAIN LOOP
# =========================
while True:

    screen_width, screen_height = screen.get_size()

    juice.update()
    bg.update(screen_height)

    speed_level = get_speed_level()  # 🎯 NEW SIGNAL

    # =========================
    # EVENTS
    # =========================
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # spawn enemies
        if not game_over and event.type == SPAWN_EVENT:
            enemy = DataEnemy()

            # pass difficulty influence indirectly via speed
            enemy.speed += speed_boost

            enemies.append(enemy)

        # restart
        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()

        # fullscreen toggle
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                fullscreen = not fullscreen

                if fullscreen:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

    # =========================
    # SHAKE
    # =========================
    shake_x, shake_y = juice.get_shake_offset()

    # =========================
    # FRAME BUFFER
    # =========================
    frame = pygame.Surface((screen_width, screen_height))
    frame.fill((10, 12, 20))

    # =========================
    # BACKGROUND (LOW PRIORITY LAYER)
    # =========================
    bg.draw(frame)

    # =========================
    # GAMEPLAY
    # =========================
    if not game_over:

        player.update()

        # pass readability state into player (future use)
        player.speed_level = speed_level

        for enemy in enemies[:]:
            enemy.update()

            # pass readability state into enemy (future use)
            enemy.speed_level = speed_level

            if enemy.collides(player):
                game_over = True
                juice.trigger_hit()

            if enemy.y > screen_height:
                enemies.remove(enemy)
                score.add_survival()

        # difficulty scaling
        if pygame.time.get_ticks() % 2500 < 16:
            speed_boost += 0.5

        # =========================
        # DRAW ORDER (CLARITY FIRST)
        # =========================

        # player ALWAYS on top clarity layer
        player.draw(frame)

        # enemies simplified depending on speed_level (handled in enemy.py next step)
        for enemy in enemies:
            enemy.draw(frame)

        score.draw(frame)

    # =========================
    # GAME OVER SCREEN
    # =========================
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

    pygame.display.update()
    clock.tick(60)