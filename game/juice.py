import pygame
import random


class JuiceEngine:

    def __init__(self):

        # screen shake
        self.shake_intensity = 0
        self.shake_timer = 0

        # flash overlay
        self.flash_alpha = 0

        # slow motion
        self.slowmo_timer = 0
        self.slowmo_factor = 1

        # particles
        self.particles = []


    # =========================
    # TRIGGERS
    # =========================

    def trigger_hit(self):

        # screen shake
        self.shake_intensity = 8
        self.shake_timer = 10

        # red flash
        self.flash_alpha = 120

        # slow motion (0.15 sec)
        self.slowmo_timer = 10
        self.slowmo_factor = 0.3

        # particles
        self.spawn_particles(15)


    def trigger_combo(self):

        self.spawn_particles(10)


    # =========================
    # PARTICLES
    # =========================

    def spawn_particles(self, count):

        for _ in range(count):

            self.particles.append({
                "x": random.randint(300, 500),
                "y": random.randint(200, 300),
                "vx": random.uniform(-3, 3),
                "vy": random.uniform(-3, 3),
                "life": random.randint(20, 40),
                "color": (0, 255, 200)
            })


    # =========================
    # UPDATE
    # =========================

    def update(self):

        # shake decay
        if self.shake_timer > 0:
            self.shake_timer -= 1
        else:
            self.shake_intensity = 0

        # flash fade
        if self.flash_alpha > 0:
            self.flash_alpha -= 10

        # slow motion decay
        if self.slowmo_timer > 0:
            self.slowmo_timer -= 1
            self.slowmo_factor = 0.3
        else:
            self.slowmo_factor = 1

        # particles update
        for p in self.particles[:]:

            p["x"] += p["vx"]
            p["y"] += p["vy"]
            p["life"] -= 1

            if p["life"] <= 0:
                self.particles.remove(p)


    # =========================
    # SCREEN SHAKE OFFSET
    # =========================

    def get_shake_offset(self):

        if self.shake_intensity <= 0:
            return (0, 0)

        import random

        return (
            random.randint(-self.shake_intensity, self.shake_intensity),
            random.randint(-self.shake_intensity, self.shake_intensity)
        )


    # =========================
    # DRAW OVERLAYS
    # =========================

    def draw(self, screen):

        # RED FLASH
        if self.flash_alpha > 0:

            overlay = pygame.Surface(screen.get_size())
            overlay.set_alpha(self.flash_alpha)
            overlay.fill((255, 0, 0))
            screen.blit(overlay, (0, 0))

        # PARTICLES
        for p in self.particles:

            pygame.draw.circle(
                screen,
                p["color"],
                (int(p["x"]), int(p["y"])),
                3
            )