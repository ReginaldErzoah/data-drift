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

        # movement direction
        self.direction = 0

    # =========================
    # UPDATE MOVEMENT
    # =========================
    def update(self):
        keys = pygame.key.get_pressed()
        prev_x = self.x

        if keys[pygame.K_LEFT]:
            self.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        # dynamic screen width
        screen_width = (
            pygame.display.get_surface()
            .get_width()
        )

        # keep player inside screen
        self.x = max(
            0,
            min(
                self.x,
                screen_width - self.width
            )
        )

        # update vertical position
        self.update_position()

        # animation timer
        self.t += 0.25

        # trail tracking
        self.trail.append(self.x)
        if len(self.trail) > 10:
            self.trail.pop(0)

        # direction for lean animation
        self.direction = self.x - prev_x




    # =========================
    # RESPONSIVE POSITION
    # =========================
    def update_position(self):
        screen_height = (
            pygame.display.get_surface()
            .get_height()
        )
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
        # TRAIL (DATA STREAM EFFECT)
        # =========================
        for i, tx in enumerate(self.trail):

            size = int(
                6 + i * 0.6
            )

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
        bounce = int(
            3 * math.sin(self.t * 2)
        )

        # =========================
        # LEAN EFFECT
        # =========================
        lean = 0
        if self.direction > 0:
            lean = 2
        elif self.direction < 0:
            lean = -2

        # =========================
        # CORE PLAYER
        # =========================
        cx = self.x + lean
        cy = self.y + bounce

        # outer glow
        pygame.draw.circle(
            screen,
            (0, 255, 200),
            (
                cx + self.width // 2,
                cy + self.height // 2
            ),
            26
        )

        # inner data core
        pygame.draw.circle(
            screen,
            (0, 200, 170),
            (
                cx + self.width // 2,
                cy + self.height // 2
            ),
            16
        )

        # analyst dashboard screen
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

        # mini data visualization line
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