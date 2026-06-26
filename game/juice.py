import pygame
import random


class JuiceEngine:

    def __init__(self):

        # =========================
        # SCREEN SHAKE
        # =========================
        self.shake_intensity = 0
        self.shake_decay = 0.85  # smooth decay factor

        # =========================
        # FLASH EFFECT
        # =========================
        self.flash_alpha = 0
        self.flash_decay = 0.88  # smoother fade-out

        # =========================
        # SLOW MOTION (reserved for future use)
        # =========================
        self.slowmo_factor = 1

        # =========================
        # PARTICLES
        # =========================
        self.particles = []


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
                "vx": random.uniform(-3, 3),
                "vy": random.uniform(-3, 3),
                "life": random.randint(25, 50),
                "color": (0, 255, 200)
            })


    # =========================
    # UPDATE
    # =========================
    def update(self):

        # -------------------------
        # SHAKE (smooth decay)
        # -------------------------
        self.shake_intensity *= self.shake_decay
        if self.shake_intensity < 0.2:
            self.shake_intensity = 0

        # -------------------------
        # FLASH (smooth fade)
        # -------------------------
        self.flash_alpha *= self.flash_decay
        if self.flash_alpha < 2:
            self.flash_alpha = 0

        # -------------------------
        # SLOWMO (simple decay back to normal)
        # -------------------------
        if self.slowmo_factor < 1:
            self.slowmo_factor += 0.02
        if self.slowmo_factor > 1:
            self.slowmo_factor = 1

        # -------------------------
        # PARTICLES
        # -------------------------
        for p in self.particles[:]:

            p["x"] += p["vx"]
            p["y"] += p["vy"]
            p["life"] -= 1

            # fade out velocity slightly
            p["vx"] *= 0.98
            p["vy"] *= 0.98

            if p["life"] <= 0:
                self.particles.remove(p)


    # =========================
    # SHAKE OFFSET
    # =========================
    def get_shake_offset(self):

        if self.shake_intensity <= 0:
            return 0, 0

        return (
            random.randint(-int(self.shake_intensity), int(self.shake_intensity)),
            random.randint(-int(self.shake_intensity), int(self.shake_intensity))
        )


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

        # PARTICLES
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
        self.particles.clear()
        self.slowmo_factor = 1