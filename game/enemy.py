import pygame
import random
import math

class DataEnemy:

    # Lanes ensure full screen coverage (prevents corner exploits)
    LANES = [0, 80, 160, 240, 320, 400, 480, 560, 640, 720]

    def __init__(self):
        self.x = random.choice(self.LANES)
        self.y = -40
        self.speed = random.randint(3, 5)
        self.t = 0

        self.size = 40  # IMPORTANT: consistent hitbox reference

        self.type = random.choice(["NULL", "DUP", "OUTLIER", "TYPE"])

    def update(self):
        self.y += self.speed
        self.t += 0.2

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
    # 🔴 NULL → Empty Cell
    # =========================
    def draw_null(self, screen):
        pulse = int(2 * math.sin(self.t * 3))

        pygame.draw.rect(
            screen,
            (255, 80, 80),
            (self.x, self.y, self.size, self.size),
            2
        )

        pygame.draw.rect(
            screen,
            (60, 0, 0),
            (self.x + 6, self.y + 6, self.size - 12, self.size - 12),
            1
        )

        if int(self.t * 4) % 2 == 0:
            pygame.draw.circle(
                screen,
                (255, 120, 120),
                (self.x + self.size // 2, self.y + self.size // 2),
                3 + pulse
            )

    # =========================
    # 🟠 DUP → Duplicate Rows
    # =========================
    def draw_dup(self, screen):
        offset = int(2 * math.sin(self.t * 2))

        pygame.draw.rect(
            screen,
            (255, 170, 0),
            (self.x, self.y, self.size, self.size // 2),
            2
        )

        pygame.draw.rect(
            screen,
            (255, 200, 80),
            (self.x + offset, self.y + self.size // 2, self.size, self.size // 2),
            2
        )

        pygame.draw.line(
            screen,
            (255, 200, 80),
            (self.x + 5, self.y + 10),
            (self.x + self.size - 5, self.y + 10),
            1
        )

    # =========================
    # 🟣 OUTLIER → Chart Spike
    # =========================
    def draw_outlier(self, screen):
        spike = int(4 * math.sin(self.t * 4))

        bars = [10, 18, 12, 35 + spike, 14]

        for i, h in enumerate(bars):
            color = (180, 0, 255) if i != 3 else (255, 80, 255)

            pygame.draw.rect(
                screen,
                color,
                (self.x + i * 6, self.y + self.size - h, 4, h)
            )

    # =========================
    # 🟡 TYPE ERROR → Broken Column
    # =========================
    def draw_type_error(self, screen):
        flicker = int(2 * math.sin(self.t * 5))

        pygame.draw.rect(
            screen,
            (255, 255, 0),
            (self.x, self.y, self.size, self.size),
            2
        )

        pygame.draw.rect(
            screen,
            (120, 120, 0),
            (self.x, self.y + 15, self.size, self.size - 15),
            1
        )

        pygame.draw.polygon(screen, (255, 255, 0), [
            (self.x + self.size - 8, self.y + 3),
            (self.x + self.size - 2, self.y + 12),
            (self.x + self.size - 14, self.y + 12)
        ])

    def collides(self, player):
        return (
            self.x < player.x + player.width and
            self.x + self.size > player.x and
            self.y < player.y + player.height and
            self.y + self.size > player.y
        )