import pygame
import math
import random


class Background:

    def __init__(self):

        # scrolling offset for moving grid
        self.scroll_y = 0

        # subtle data noise particles
        self.particles = []

        for _ in range(40):
            self.particles.append(self._create_particle())


    # =========================
    # CREATE DATA PARTICLES
    # =========================
    def _create_particle(self):

        return {
            "x": random.randint(0, 800),
            "y": random.randint(0, 500),
            "speed": random.uniform(0.2, 1.0),
            "alpha": random.randint(30, 120)
        }


    # =========================
    # UPDATE BACKGROUND
    # =========================
    def update(self, screen_height):

        self.scroll_y += 0.5

        if self.scroll_y > 40:
            self.scroll_y = 0

        # update particles
        for p in self.particles:

            p["y"] += p["speed"]

            if p["y"] > screen_height:
                p["y"] = 0
                p["x"] = random.randint(0, 800)


    # =========================
    # DRAW GRID (EXCEL STYLE)
    # =========================
    def draw_grid(self, screen):

        width = screen.get_width()
        height = screen.get_height()

        grid_color = (25, 30, 45)

        cell_size = 40


        # vertical lines
        for x in range(0, width, cell_size):

            pygame.draw.line(
                screen,
                grid_color,
                (x, 0),
                (x, height),
                1
            )


        # horizontal lines (with scroll effect)
        for y in range(0, height, cell_size):

            offset_y = (y + self.scroll_y) % height

            pygame.draw.line(
                screen,
                grid_color,
                (0, offset_y),
                (width, offset_y),
                1
            )


    # =========================
    # DRAW DATA LAYER (FOREGROUND ATMOSPHERE)
    # =========================
    def draw_data_layer(self, screen):

        for p in self.particles:

            alpha_surface = pygame.Surface((3, 3))

            alpha_surface.set_alpha(p["alpha"])

            alpha_surface.fill((0, 180, 150))

            screen.blit(alpha_surface, (p["x"], p["y"]))


    # =========================
    # MASTER DRAW FUNCTION
    # =========================
    def draw(self, screen):

        # dark base background
        screen.fill((10, 12, 20))

        # grid layer (back)
        self.draw_grid(screen)

        # data noise layer (middle)
        self.draw_data_layer(screen)