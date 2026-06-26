import pygame
import random
import math


class DataEnemy:

    def __init__(self, screen_width=800):

        self.screen_width = screen_width

        # spawn anywhere across FULL width
        self.x = random.uniform(0, screen_width - 42)
        self.y = -40

        self.speed = random.randint(3, 5)

        self.t = 0
        self.size = 42

        self.type = random.choice(
            ["NULL", "DUP", "OUTLIER", "TYPE"]
        )

        self.speed_level = "NORMAL"

    # =========================
    # UPDATE
    # =========================
    def update(self):
        self.y += self.speed
        self.t += 0.25

    # =========================
    # DRAW ROUTER (RESTORED FULL VISUALS)
    # =========================
    def draw(self, screen):

        if self.type == "NULL":
            self.draw_null(screen)

        elif self.type == "DUP":
            self.draw_dup(screen)

        elif self.type == "OUTLIER":
            self.draw_outlier(screen)

        else:
            self.draw_type_error(screen)

    # =========================
    # NULL
    # =========================
    def draw_null(self, screen):

        pygame.draw.rect(
            screen,
            (255, 80, 80),
            (self.x, self.y, self.size, self.size),
            3
        )

    # =========================
    # DUP
    # =========================
    def draw_dup(self, screen):

        pygame.draw.rect(
            screen,
            (255, 170, 0),
            (self.x, self.y, self.size, self.size // 2),
            3
        )

        pygame.draw.rect(
            screen,
            (255, 210, 80),
            (self.x, self.y + self.size // 2, self.size, self.size // 2),
            3
        )

    # =========================
    # OUTLIER
    # =========================
    def draw_outlier(self, screen):

        spike = int(5 * math.sin(self.t * 4))

        bars = [8, 14, 10, 34 + spike, 12]

        for i, h in enumerate(bars):

            color = (180, 0, 255) if i != 3 else (255, 80, 255)

            pygame.draw.rect(
                screen,
                color,
                (self.x + i * 7, self.y + self.size - h, 5, h)
            )

    # =========================
    # TYPE ERROR
    # =========================
    def draw_type_error(self, screen):

        flicker = int(2 * math.sin(self.t * 5))
        jitter_x = self.x + flicker

        pygame.draw.rect(
            screen,
            (255, 255, 0),
            (jitter_x, self.y, self.size, self.size),
            3
        )

        pygame.draw.rect(
            screen,
            (120, 120, 0),
            (jitter_x, self.y + 15, self.size, self.size - 15),
            2
        )

        pygame.draw.polygon(
            screen,
            (255, 255, 0),
            [
                (jitter_x + self.size - 8, self.y + 3),
                (jitter_x + self.size - 2, self.y + 12),
                (jitter_x + self.size - 14, self.y + 12)
            ]
        )

    # =========================
    # COLLISION
    # =========================
    def collides(self, player):

        return (
            self.x < player.x + player.width
            and self.x + self.size > player.x
            and self.y < player.y + player.height
            and self.y + self.size > player.y
        )