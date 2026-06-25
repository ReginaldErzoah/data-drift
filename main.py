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

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT),
    pygame.RESIZABLE
)

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
# RESTART FUNCTION
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

    juice.update()
    bg.update(screen.get_height())

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
    # DRAW
    # =========================
    screen.fill((10, 12, 20))
    bg.draw(screen)

    if not game_over:

        player.update()

        for enemy in enemies[:]:
            enemy.update()

            if enemy.collides(player):
                game_over = True
                juice.trigger_hit()

            if enemy.y > screen.get_height():
                enemies.remove(enemy)
                score.add_survival()

        if pygame.time.get_ticks() % 2500 < 16:
            speed_boost += 0.5

        # =========================
        # APPLY SHAKE (VISUAL ONLY)
        # =========================
        temp_surface = pygame.Surface(screen.get_size())

        temp_surface.blit(screen, (0, 0))

        player.draw(temp_surface)

        for enemy in enemies:
            enemy.draw(temp_surface)

        score.draw(temp_surface)

        screen.blit(temp_surface, (shake_x, shake_y))

    else:

        if score.get_score() > high_score:
            high_score = score.get_score()

        score.draw_final_score(screen)

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

        screen.blit(high_text, (
            screen.get_width() // 2 - high_text.get_width() // 2,
            300
        ))

        screen.blit(hint, (
            screen.get_width() // 2 - hint.get_width() // 2,
            340
        ))

    juice.draw(screen)

    pygame.display.update()
    clock.tick(60)