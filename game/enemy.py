import pygame
import random
import math


class DataEnemy:

    def __init__(self, screen_width=800):

        self.screen_width = screen_width

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
    # UPDATE SCREEN WIDTH (important for resize)
    # =========================
    def update_screen_width(self, width):
        self.screen_width = width

    # =========================
    # UPDATE
    # =========================
    def update(self):
        self.y += self.speed
        self.t += 0.25

    # =========================
    # READABILITY MODE
    # =========================
    def readability_mode(self):

        if hasattr(self, "speed_level"):

            if self.speed_level == "CRITICAL":
                return 2
            elif self.speed_level == "FAST":
                return 1

        if self.speed >= 8:
            return 2
        elif self.speed >= 5:
            return 1
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
    # NULL
    # =========================
    def draw_null(self, screen, mode):

        if mode == 2:
            pygame.draw.rect(screen, (255, 80, 80), (self.x, self.y, self.size, self.size), 3)
            return

        pygame.draw.rect(screen, (255, 80, 80), (self.x, self.y, self.size, self.size), 3)

    # =========================
    # DUP
    # =========================
    def draw_dup(self, screen, mode):

        pygame.draw.rect(screen, (255, 170, 0), (self.x, self.y, self.size, self.size), 3)

    # =========================
    # OUTLIER
    # =========================
    def draw_outlier(self, screen, mode):

        pygame.draw.rect(screen, (180, 0, 255), (self.x, self.y, self.size, self.size), 3)

    # =========================
    # TYPE ERROR
    # =========================
    def draw_type_error(self, screen, mode):

        pygame.draw.rect(screen, (255, 255, 0), (self.x, self.y, self.size, self.size), 3)

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