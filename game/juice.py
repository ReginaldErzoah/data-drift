import pygame
import random
import math


class JuiceEngine:

    def __init__(self):

        # =========================
        # SCREEN SHAKE
        # =========================
        self.shake_intensity = 0
        self.shake_decay = 0.88  # slightly smoother than before
        self.shake_seed = random.random() * 1000

        # =========================
        # FLASH EFFECT
        # =========================
        self.flash_alpha = 0
        self.flash_decay = 0.86

        # =========================
        # SLOW MOTION
        # =========================
        self.slowmo_factor = 1

        # =========================
        # PARTICLES
        # =========================
        self.particles = []

        # frame counter for stable motion
        self.t = 0


    # =========================
    # TRIGGERS
    # =========================
    def trigger_hit(self):
        self.shake_intensity = 10
        self.flash_alpha = 140
        self.slowmo_factor = 0.35

        self.spawn_particles(18)


    def trigger_combo(self):
        self.spawn_particles(10)


    # =========================
    # PARTICLES
    # =========================
    def spawn_particles(self, count, screen_w=800, screen_h=500):

        for _ in range(count):

            self.particles.append({
                "x": random.randint(0, screen_w),
                "y": random.randint(0, screen_h),
                "vx": random.uniform(-2.5, 2.5),
                "vy": random.uniform(-2.5, 2.5),
                "life": random.randint(25, 50),
                "color": (0, 255, 200),
                "alpha": 255
            })


    # =========================
    # UPDATE
    # =========================
    def update(self):

        self.t += 1

        # -------------------------
        # SHAKE (smooth decay)
        # -------------------------
        self.shake_intensity *= self.shake_decay
        if self.shake_intensity < 0.15:
            self.shake_intensity = 0

        # -------------------------
        # FLASH (smooth fade)
        # -------------------------
        self.flash_alpha *= self.flash_decay
        if self.flash_alpha < 1:
            self.flash_alpha = 0

        # -------------------------
        # SLOWMO (return to normal)
        # -------------------------
        if self.slowmo_factor < 1:
            self.slowmo_factor += 0.015
        if self.slowmo_factor > 1:
            self.slowmo_factor = 1

        # -------------------------
        # PARTICLES (stable motion)
        # -------------------------
        for p in self.particles[:]:

            p["x"] += p["vx"]
            p["y"] += p["vy"]

            p["vx"] *= 0.97
            p["vy"] *= 0.97

            p["life"] -= 1
            p["alpha"] = max(0, p.get("alpha", 255) - 8)

            if p["life"] <= 0:
                self.particles.remove(p)


    # =========================
    # SHAKE OFFSET (SMOOTHER THAN RANDOM JITTER)
    # =========================
    def get_shake_offset(self):

        if self.shake_intensity <= 0:
            return 0, 0

        # smooth pseudo-noise instead of pure random jitter
        offset_x = math.sin(self.t * 0.9 + self.shake_seed) * self.shake_intensity
        offset_y = math.cos(self.t * 1.1 + self.shake_seed) * self.shake_intensity

        return int(offset_x), int(offset_y)


    # =========================
    # DRAW
    # =========================
    def draw(self, screen):

        # FLASH OVERLAY
        if self.flash_alpha > 1:

            overlay = pygame.Surface(screen.get_size())
            overlay.set_alpha(int(self.flash_alpha))
            overlay.fill((255, 0, 0))
            screen.blit(overlay, (0, 0))

        # PARTICLES (slightly smoother rendering)
        for p in self.particles:

            pygame.draw.circle(
                screen,
                p["color"],
                (int(p["x"]), int(p["y"])),
                3
            )


    # =========================
    # RESET
    # =========================
    def reset(self):

        self.shake_intensity = 0
        self.flash_alpha = 0
        self.slowmo_factor = 1
        self.particles.clear()
        self.t = 0