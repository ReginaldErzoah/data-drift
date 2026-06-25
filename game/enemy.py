import pygame
import random
import math


class DataEnemy:

    # Lanes ensure full screen coverage (prevents corner exploits)
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


    # =========================
    # UPDATE
    # =========================
    def update(self):

        self.y += self.speed
        self.t += 0.25


    # =========================
    # DRAW ROUTER
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
    # 🔴 NULL (MISSING DATA)
    # =========================
    def draw_null(self, screen):

        pulse = int(2 * math.sin(self.t * 3))

        # strong outer frame
        pygame.draw.rect(
            screen,
            (255, 80, 80),
            (self.x, self.y, self.size, self.size),
            3
        )

        # missing core (key identity)
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

        # blinking “null signal”
        if int(self.t * 4) % 2 == 0:
            pygame.draw.circle(
                screen,
                (255, 140, 140),
                (
                    self.x + self.size // 2,
                    self.y + self.size // 2
                ),
                3 + pulse
            )


    # =========================
    # 🟠 DUP (DUPLICATE DATA)
    # =========================
    def draw_dup(self, screen):

        offset = int(2 * math.sin(self.t * 2))

        # row 1
        pygame.draw.rect(
            screen,
            (255, 170, 0),
            (self.x, self.y, self.size, self.size // 2),
            3
        )

        # row 2 (duplicate shifted)
        pygame.draw.rect(
            screen,
            (255, 210, 80),
            (
                self.x + offset,
                self.y + self.size // 2,
                self.size,
                self.size // 2
            ),
            3
        )

        # duplication separator
        pygame.draw.line(
            screen,
            (255, 220, 120),
            (self.x + 4, self.y + self.size // 2),
            (self.x + self.size - 4, self.y + self.size // 2),
            2
        )


    # =========================
    # 🟣 OUTLIER (SPIKE DATA)
    # =========================
    def draw_outlier(self, screen):

        spike = int(5 * math.sin(self.t * 4))

        bars = [8, 14, 10, 34 + spike, 12]

        for i, h in enumerate(bars):

            color = (180, 0, 255) if i != 3 else (255, 80, 255)

            pygame.draw.rect(
                screen,
                color,
                (
                    self.x + i * 7,
                    self.y + self.size - h,
                    5,
                    h
                )
            )

        # spike highlight
        pygame.draw.circle(
            screen,
            (255, 120, 255),
            (
                self.x + 21,
                self.y + self.size - (34 + spike)
            ),
            4
        )


    # =========================
    # 🟡 TYPE ERROR (SCHEMA BREAK)
    # =========================
    def draw_type_error(self, screen):

        flicker = int(2 * math.sin(self.t * 5))

        jitter_x = self.x + flicker

        # corrupted block
        pygame.draw.rect(
            screen,
            (255, 255, 0),
            (jitter_x, self.y, self.size, self.size),
            3
        )

        # broken structure
        pygame.draw.rect(
            screen,
            (120, 120, 0),
            (
                jitter_x,
                self.y + 15,
                self.size,
                self.size - 15
            ),
            2
        )

        # warning icon
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