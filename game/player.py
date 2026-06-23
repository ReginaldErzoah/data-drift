import pygame
import math

class Player:
    def __init__(self):
        self.x = 380
        self.y = 420
        self.width = 44
        self.height = 44
        self.speed = 7

        # animation state
        self.t = 0
        self.trail = []  # stores past positions

    def update(self):
        keys = pygame.key.get_pressed()

        prev_x = self.x

        if keys[pygame.K_LEFT]:
            self.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        self.x = max(0, min(self.x, 800 - self.width))

        # update animation timer
        self.t += 0.25

        # store trail positions
        self.trail.append(self.x)

        if len(self.trail) > 10:
            self.trail.pop(0)

        # store direction (for lean effect)
        self.direction = self.x - prev_x

    def draw(self, screen):

        # =========================
        # TRAIL (DATA STREAM EFFECT)
        # =========================
        for i, tx in enumerate(self.trail):
            alpha = int(255 * (i / len(self.trail)))
            size = int(6 + i * 0.6)

            pygame.draw.circle(
                screen,
                (0, 200, 180),
                (tx + 22, self.y + 22),
                size,
                1
            )

        # =========================
        # BOUNCE EFFECT (RUN FEEL)
        # =========================
        bounce = int(3 * math.sin(self.t * 2))

        # =========================
        # LEAN EFFECT (DIRECTIONAL MOTION)
        # =========================
        lean = 0
        if hasattr(self, "direction"):
            if self.direction > 0:
                lean = 2
            elif self.direction < 0:
                lean = -2

        # =========================
        # CORE PLAYER (DATA NODE)
        # =========================
        cx = self.x + lean
        cy = self.y + bounce

        # glow base
        pygame.draw.circle(
            screen,
            (0, 255, 200),
            (cx + 22, cy + 22),
            26
        )

        # inner body
        pygame.draw.circle(
            screen,
            (0, 200, 170),
            (cx + 22, cy + 22),
            16
        )

        # analysis screen (identity)
        pygame.draw.rect(
            screen,
            (10, 20, 35),
            (cx + 10, cy + 8, 28, 18),
            border_radius=3
        )

        # mini “data line”
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