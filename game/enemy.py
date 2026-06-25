import pygame
import random
import math


class DataEnemy:

    LANES = [i for i in range(0, 760, 80)]

    def __init__(self):

        self.x = random.choice(self.LANES)
        self.y = -40

        self.speed = random.randint(3, 5)

        self.t = 0
        self.size = 42

        self.type = random.choice(
            ["NULL", "DUP", "OUTLIER", "TYPE"]
        )

        # NEW: external readability override (from main.py)
        self.speed_level = "NORMAL"

    # =========================
    # UPDATE
    # =========================
    def update(self):
        self.y += self.speed
        self.t += 0.25

    # =========================
    # READABILITY MODE (ENHANCED SYSTEM)
    # =========================
    def readability_mode(self):

        # PRIORITY: external system (main.py)
        if hasattr(self, "speed_level"):

            if self.speed_level == "CRITICAL":
                return 2  # ICON MODE (maximum clarity)

            elif self.speed_level == "FAST":
                return 1  # SIMPLIFIED MODE

        # fallback: internal speed logic
        if self.speed >= 8:
            return 2
        elif self.speed >= 5:
            return 1
        else:
            return 0

    # =========================
    # DRAW ROUTER
    # =========================
    def draw(self, screen):

        mode = self.readability_mode()

        if self.type == "NULL":
            self.draw_null(screen, mode)

        elif self.type == "DUP":
            self.draw_dup(screen, mode)

        elif self.type == "OUTLIER":
            self.draw_outlier(screen, mode)

        else:
            self.draw_type_error(screen, mode)

    # =========================
    # NULL (MISSING DATA)
    # =========================
    def draw_null(self, screen, mode):

        # ICON MODE → ultra readable block
        if mode == 2:
            pygame.draw.rect(
                screen,
                (255, 80, 80),
                (self.x, self.y, self.size, self.size),
                3
            )
            return

        # SIMPLIFIED MODE
        if mode == 1:
            pygame.draw.rect(
                screen,
                (255, 80, 80),
                (self.x, self.y, self.size, self.size),
                3
            )
            pygame.draw.circle(
                screen,
                (255, 140, 140),
                (self.x + 21, self.y + 21),
                3
            )
            return

        # DETAILED MODE
        pulse = int(2 * math.sin(self.t * 3))

        pygame.draw.rect(
            screen,
            (255, 80, 80),
            (self.x, self.y, self.size, self.size),
            3
        )

        pygame.draw.rect(
            screen,
            (40, 0, 0),
            (
                self.x + 10,
                self.y + 10,
                self.size - 20,
                self.size - 20
            )
        )

        if int(self.t * 4) % 2 == 0:
            pygame.draw.circle(
                screen,
                (255, 140, 140),
                (self.x + 21, self.y + 21),
                3 + pulse
            )

    # =========================
    # DUP (DUPLICATE DATA)
    # =========================
    def draw_dup(self, screen, mode):

        if mode == 2:
            pygame.draw.rect(
                screen,
                (255, 170, 0),
                (self.x, self.y, self.size, self.size),
                3
            )
            return

        if mode == 1:
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
            return

        offset = int(2 * math.sin(self.t * 2))

        pygame.draw.rect(
            screen,
            (255, 170, 0),
            (self.x, self.y, self.size, self.size // 2),
            3
        )

        pygame.draw.rect(
            screen,
            (255, 210, 80),
            (self.x + offset, self.y + self.size // 2, self.size, self.size // 2),
            3
        )

        pygame.draw.line(
            screen,
            (255, 220, 120),
            (self.x + 4, self.y + self.size // 2),
            (self.x + self.size - 4, self.y + self.size // 2),
            2
        )

    # =========================
    # OUTLIER (SPIKE DATA)
    # =========================
    def draw_outlier(self, screen, mode):

        if mode == 2:
            pygame.draw.line(
                screen,
                (180, 0, 255),
                (self.x + 10, self.y + self.size - 10),
                (self.x + self.size - 10, self.y + 10),
                3
            )
            return

        if mode == 1:
            pygame.draw.rect(
                screen,
                (180, 0, 255),
                (self.x, self.y, self.size, self.size),
                3
            )
            return

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
    # TYPE ERROR (SCHEMA BREAK)
    # =========================
    def draw_type_error(self, screen, mode):

        if mode == 2:
            pygame.draw.rect(
                screen,
                (255, 255, 0),
                (self.x, self.y, self.size, self.size),
                3
            )
            return

        if mode == 1:
            pygame.draw.rect(
                screen,
                (255, 255, 0),
                (self.x, self.y, self.size, self.size),
                3
            )
            return

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