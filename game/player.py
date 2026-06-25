import pygame
import math
import random


class Player:
    def __init__(self):
        self.x = 380
        self.y = 420
        self.width = 44
        self.height = 44
        self.speed = 7

        self.bottom_margin = 30

        self.t = 0
        self.trail = []

        self.direction = 0
        self.prev_x = self.x

        # =========================
        # DEATH SYSTEM
        # =========================
        self.is_dead = False
        self.death_timer = 0
        self.particles = []

    # =========================
    # UPDATE MOVEMENT
    # =========================
    def update(self):

        # if dead → run collapse animation only
        if self.is_dead:
            self.update_death()
            return

        keys = pygame.key.get_pressed()

        self.prev_x = self.x

        if keys[pygame.K_LEFT]:
            self.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        screen_width = pygame.display.get_surface().get_width()
        self.x = max(0, min(self.x, screen_width - self.width))

        self.update_position()

        self.t += 0.25

        self.trail.append(self.x)
        if len(self.trail) > 14:
            self.trail.pop(0)

        raw_direction = self.x - self.prev_x
        self.direction = (self.direction * 0.7) + (raw_direction * 0.3)

    # =========================
    # TRIGGER DEATH
    # =========================
    def die(self):

        if self.is_dead:
            return

        self.is_dead = True
        self.death_timer = 60  # ~1 second

        # generate pixel fragments (data collapse)
        cx = self.x + self.width // 2
        cy = self.y + self.height // 2

        for _ in range(28):
            self.particles.append([
                cx,
                cy,
                random.randint(-4, 4),
                random.randint(-6, 2)
            ])

    # =========================
    # DEATH UPDATE (DATA DISSOLVE)
    # =========================
    def update_death(self):

        self.death_timer -= 1

        for p in self.particles:
            p[0] += p[2]
            p[1] += p[3]
            p[3] += 0.25  # gravity effect

        self.t += 0.3

    # =========================
    # RESPONSIVE POSITION
    # =========================
    def update_position(self):
        screen_height = pygame.display.get_surface().get_height()

        self.y = screen_height - self.height - self.bottom_margin

    # =========================
    # DRAW PLAYER
    # =========================
    def draw(self, screen):

        center_x = self.width // 2
        center_y = self.height // 2

        # =========================
        # DEATH RENDER (PIXEL DISSOLVE)
        # =========================
        if self.is_dead:

            for p in self.particles:
                pygame.draw.rect(
                    screen,
                    (0, 255, 220),
                    (p[0], p[1], 4, 4)
                )

            return

        # =========================
        # NORMAL RENDER
        # =========================

        # TRAIL
        for i, tx in enumerate(self.trail):

            fade_ratio = i / len(self.trail)
            alpha_size = int(2 + i * 0.6)

            color_intensity = int(120 + 100 * fade_ratio)

            pygame.draw.circle(
                screen,
                (0, color_intensity, 180),
                (tx + center_x, self.y + center_y),
                alpha_size,
                1
            )

        # MOTION EFFECTS
        bounce = int(3 * math.sin(self.t * 2))
        lean = int(self.direction * 0.08)

        cx = self.x + lean
        cy = self.y + bounce

        # SILHOUETTE BASE (READABILITY BOOST)
        pygame.draw.circle(
            screen,
            (0, 0, 0),
            (cx + center_x, cy + center_y),
            30
        )

        # GLOW LAYERS
        pygame.draw.circle(
            screen,
            (0, 255, 220),
            (cx + center_x, cy + center_y),
            26
        )

        pygame.draw.circle(
            screen,
            (0, 200, 180),
            (cx + center_x, cy + center_y),
            18
        )

        pygame.draw.circle(
            screen,
            (0, 140, 120),
            (cx + center_x, cy + center_y),
            12
        )

        # ANALYST HUD
        pygame.draw.rect(
            screen,
            (10, 20, 35),
            (cx + 10, cy + 8, 28, 18),
            border_radius=3
        )

        # SIGNAL LINE
        pygame.draw.lines(
            screen,
            (0, 255, 200),
            False,
            [
                (cx + 12, cy + 20),
                (cx + 18, cy + 14),
                (cx + 24, cy + 18),
                (cx + 30, cy + 12)
            ],
            2
        )

        # GROUND SHADOW
        pygame.draw.ellipse(
            screen,
            (0, 60, 50),
            (cx + 6, cy + 38, 32, 10)
        )