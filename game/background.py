import pygame
import math
import random


class Background:

    def __init__(self):

        # scroll system (smooth vertical drift)
        self.scroll_y = 0

        # adaptive particle field
        self.particles = []

        for _ in range(50):
            self.particles.append(self._create_particle(800, 500))


    # =========================
    # CREATE PARTICLES (RESPONSIVE)
    # =========================
    def _create_particle(self, width, height):

        return {
            "x": random.randint(0, width),
            "y": random.randint(0, height),
            "speed": random.uniform(0.15, 0.8),
            "alpha": random.randint(20, 90),
            "size": random.randint(1, 2)
        }


    # =========================
    # UPDATE BACKGROUND
    # =========================
    def update(self, screen_height, screen_width=800):

        # smoother parallax drift
        self.scroll_y += 0.35
        if self.scroll_y > 40:
            self.scroll_y = 0

        # update particles
        for p in self.particles:

            p["y"] += p["speed"]

            # respawn safely within dynamic width
            if p["y"] > screen_height:
                p["y"] = 0
                p["x"] = random.randint(0, screen_width)


    # =========================
    # GRID LAYER (EXCEL STYLE - OPTIMIZED)
    # =========================
    def draw_grid(self, screen):

        width = screen.get_width()
        height = screen.get_height()

        cell_size = 45  # slightly larger = less visual noise

        grid_color = (22, 26, 38)

        # vertical lines (static clarity anchors)
        for x in range(0, width, cell_size):
            pygame.draw.line(screen, grid_color, (x, 0), (x, height), 1)

        # horizontal lines (subtle scroll)
        for y in range(0, height + cell_size, cell_size):

            offset_y = (y + self.scroll_y) % (height + cell_size)

            pygame.draw.line(screen, grid_color, (0, offset_y), (width, offset_y), 1)


    # =========================
    # DATA PARTICLE LAYER (REDUCED NOISE)
    # =========================
    def draw_data_layer(self, screen):

        for p in self.particles:

            # tiny glow point (less visual clutter)
            surf = pygame.Surface((p["size"], p["size"]), pygame.SRCALPHA)

            color = (0, 180, 150, p["alpha"])
            pygame.draw.circle(
                surf,
                color,
                (p["size"] // 2, p["size"] // 2),
                p["size"]
            )

            screen.blit(surf, (p["x"], p["y"]))


    # =========================
    # MASTER DRAW FUNCTION
    # =========================
    def draw(self, screen):

        # base background (deep contrast for readability)
        screen.fill((10, 12, 20))

        # grid = structural layer (very subtle)
        self.draw_grid(screen)

        # particles = atmospheric depth (reduced intensity)
        self.draw_data_layer(screen)