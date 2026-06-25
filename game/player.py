import pygame
import math


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
    # UPDATE MOVEMENT
    # =========================
    def update(self):
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
        # TRAIL (FADE STREAM EFFECT)
        # =========================
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

        # =========================
        # BOUNCE + ENERGY EFFECT
        # =========================
        bounce = int(3 * math.sin(self.t * 2))

        # =========================
        # SMOOTH LEAN (CHARACTER FEEL)
        # =========================
        lean = int(self.direction * 0.08)

        cx = self.x + lean
        cy = self.y + bounce

        # =========================
        # SILHOUETTE CORE (IMPORTANT FOR READABILITY)
        # =========================
        pygame.draw.circle(
            screen,
            (0, 0, 0),  # shadow outline for contrast
            (cx + center_x, cy + center_y),
            30
        )

        # =========================
        # MULTI-LAYER GLOW
        # =========================

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

        # =========================
        # IDENTITY SCREEN (ANALYST HUD)
        # =========================
        pygame.draw.rect(
            screen,
            (10, 20, 35),
            (cx + 10, cy + 8, 28, 18),
            border_radius=3
        )

        # =========================
        # DATA SIGNAL LINE
        # =========================
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

        # =========================
        # BASE SHADOW (GROUND CONTACT CLARITY)
        # =========================
        pygame.draw.ellipse(
            screen,
            (0, 60, 50),
            (cx + 6, cy + 38, 32, 10)
        )