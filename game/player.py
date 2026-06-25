import pygame
import math

class Player:
    def __init__(self):
        self.x = 380
        self.y = 420
        self.width = 44
        self.height = 44
        self.speed = 7

        # distance from bottom of screen
        self.bottom_margin = 30

        # animation state
        self.t = 0

        # stores past positions
        self.trail = []

        # movement direction (smoothed)
        self.direction = 0

        # previous x for smoothing
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

        # dynamic screen width
        screen_width = pygame.display.get_surface().get_width()

        # keep player inside screen
        self.x = max(0, min(self.x, screen_width - self.width))

        # update vertical position
        self.update_position()

        # animation timer
        self.t += 0.25

        # trail tracking
        self.trail.append(self.x)
        if len(self.trail) > 14:   # slightly longer trail
            self.trail.pop(0)

        # smoother direction (instead of instant flip)
        raw_direction = self.x - self.prev_x
        self.direction = (self.direction * 0.7) + (raw_direction * 0.3)


    # =========================
    # RESPONSIVE POSITION
    # =========================
    def update_position(self):
        screen_height = pygame.display.get_surface().get_height()

        self.y = (
            screen_height
            - self.height
            - self.bottom_margin
        )


    # =========================
    # DRAW PLAYER
    # =========================
    def draw(self, screen):

        # =========================
        # TRAIL (IMPROVED DATA STREAM)
        # =========================
        for i, tx in enumerate(self.trail):

            fade = i / len(self.trail)
            size = int(2 + i * 0.5)

            pygame.draw.circle(
                screen,
                (0, 200, 180),
                (
                    tx + self.width // 2,
                    self.y + self.height // 2
                ),
                size,
                1
            )


        # =========================
        # BOUNCE EFFECT
        # =========================
        bounce = int(3 * math.sin(self.t * 2))


        # =========================
        # SMOOTH LEAN EFFECT
        # =========================
        lean = int(self.direction * 0.08)


        # =========================
        # CORE PLAYER POSITION
        # =========================
        cx = self.x + lean
        cy = self.y + bounce


        # =========================
        # IMPROVED MULTI-LAYER GLOW
        # =========================

        # outer glow (soft aura)
        pygame.draw.circle(
            screen,
            (0, 255, 220),
            (cx + self.width // 2, cy + self.height // 2),
            28
        )

        # mid glow
        pygame.draw.circle(
            screen,
            (0, 200, 180),
            (cx + self.width // 2, cy + self.height // 2),
            20
        )

        # core body
        pygame.draw.circle(
            screen,
            (0, 140, 120),
            (cx + self.width // 2, cy + self.height // 2),
            14
        )


        # =========================
        # IDENTITY SCREEN (DATA ANALYST HUD)
        # =========================
        pygame.draw.rect(
            screen,
            (10, 20, 35),
            (
                cx + 10,
                cy + 8,
                28,
                18
            ),
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