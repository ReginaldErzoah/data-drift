import pygame
import sys

from game.player import Player
from game.enemy import DataEnemy
from game.score import Score


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

# =========================
# HIGH SCORE (IN MEMORY)
# =========================
high_score = 0

# =========================
# SPAWN SYSTEM
# =========================
SPAWN_EVENT = pygame.USEREVENT + 1

pygame.time.set_timer(
    SPAWN_EVENT,
    900
)

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

    global player
    global enemies
    global score
    global game_over
    global speed_boost

    player = Player()
    enemies.clear()
    score.reset()
    game_over = False
    speed_boost = 0

# =========================
# MAIN LOOP
# =========================
while True:
    screen.fill(
        (10, 12, 20)
    )

    # =========================
    # EVENTS
    # =========================
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()


        # Spawn enemies
        if (
            not game_over
            and event.type == SPAWN_EVENT
        ):

            enemy = DataEnemy()

            enemy.speed += speed_boost

            enemies.append(enemy)

        # Restart
        if (
            game_over
            and event.type == pygame.KEYDOWN
        ):
            if event.key == pygame.K_r:
                restart_game()



        # Fullscreen toggle
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode(
                        (0, 0),
                        pygame.FULLSCREEN
                    )
                else:
                    screen = pygame.display.set_mode(
                        (WIDTH, HEIGHT),
                        pygame.RESIZABLE
                    )

    # =========================
    # ACTIVE GAME
    # =========================
    if not game_over:
        player.update()
        for enemy in enemies[:]:
            enemy.update()
            enemy.draw(screen)

            # collision
            if enemy.collides(player):
                game_over = True



        # survived
            if enemy.y > screen.get_height():
                enemies.remove(enemy)
                score.add_survival()

        # difficulty scaling
        if pygame.time.get_ticks() % 2500 < 16:
            speed_boost += 0.5

        player.draw(screen)
        score.draw(screen)

    # =========================
    # GAME OVER SCREEN
    # =========================
    else:
        # update high score
        if score.get_score() > high_score:
            high_score = score.get_score()

        # draw final score + high score
        score.draw_final_score(screen)

        font = pygame.font.SysFont(
            "Arial",
            22
        )

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

        screen.blit(
            high_text,
            (
                screen.get_width() // 2
                - high_text.get_width() // 2,

                300
            )
        )

        screen.blit(
            hint,
            (
                screen.get_width() // 2
                - hint.get_width() // 2,

                340
            )
        )

    pygame.display.update()
    clock.tick(60)