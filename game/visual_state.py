import pygame
import random


class VisualState:
    """
    Central controller for global visual intensity.

    Handles:
    - screen flash (damage / impact)
    - slow motion moments
    - global intensity scaling (based on game pressure)
    - optional screen dimming / color tinting
    """

    def __init__(self):
        # =========================
        # FLASH SYSTEM
        # =========================
        self.flash_alpha = 0
        self.flash_color = (255, 0, 0)

        # =========================
        # SLOW MOTION
        # =========================
        self.slowmo_timer = 0
        self.slowmo_factor = 1.0

        # =========================
        # GLOBAL INTENSITY
        # =========================
        self.intensity = 0.0  # ramps with difficulty

        # =========================
        # SCREEN SHAKE (LIGHT SUPPORT)
        # =========================
        self.shake_strength = 0

    # =========================
    # UPDATE
    # =========================
    def update(self, score_value=0, speed_boost=0):

        # intensity ramps naturally over time
        target_intensity = min(1.0, (score_value / 100.0) + (speed_boost / 20.0))
        self.intensity += (target_intensity - self.intensity) * 0.05

        # slow motion decay
        if self.slowmo_timer > 0:
            self.slowmo_timer -= 1
            self.slowmo_factor = 0.6
        else:
            self.slowmo_factor = 1.0

        # flash decay
        if self.flash_alpha > 0:
            self.flash_alpha -= 10
            if self.flash_alpha < 0:
                self.flash_alpha = 0

        # shake decay
        self.shake_strength *= 0.85

    # =========================
    # TRIGGERS
    # =========================

    def trigger_hit(self):
        """Call when player collides with enemy"""
        self.flash_alpha = 160
        self.shake_strength = 10
        self.slowmo_timer = 8  # ~0.1–0.2s freeze feel

    def trigger_combo(self):
        """Optional: for score milestones"""
        self.flash_alpha = 80
        self.shake_strength = 5

    # =========================
    # SHAKE OFFSET
    # =========================
    def get_shake_offset(self):
        if self.shake_strength <= 0:
            return 0, 0

        return (
            random.randint(-int(self.shake_strength), int(self.shake_strength)),
            random.randint(-int(self.shake_strength), int(self.shake_strength))
        )

    # =========================
    # APPLY VISUAL OVERLAY
    # =========================
    def draw(self, screen):

        if self.flash_alpha <= 0:
            return

        overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)

        overlay.fill(
            (
                self.flash_color[0],
                self.flash_color[1],
                self.flash_color[2],
                self.flash_alpha
            )
        )

        screen.blit(overlay, (0, 0))

    # =========================
    # GETTERS
    # =========================
    def get_slowmo_factor(self):
        return self.slowmo_factor

    def get_intensity(self):
        return self.intensity