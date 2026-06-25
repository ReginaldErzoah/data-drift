import pygame

class Score:

    def __init__(self):
        self.value = 0
        self.font = pygame.font.SysFont("Arial", 24)
        self.large_font = pygame.font.SysFont("Arial", 48)

    # =========================
    # SCORE UPDATE
    # =========================

    def add_survival(self):
        self.value += 1

    # =========================
    # GET FINAL SCORE
    # =========================

    def get_score(self):
        return self.value

    # =========================
    # RESET GAME
    # =========================

    def reset(self):
        self.value = 0

    # =========================
    # IN-GAME HUD
    # =========================

    def draw(self, screen):

        text = self.font.render(
            f"Score: {self.value}",
            True,
            (255, 255, 255)
        )

        screen.blit(text, (10, 10))

    # =========================
    # GAME OVER SCREEN SCORE
    # =========================

    def draw_final_score(self, screen):

        title = self.large_font.render(
            "GAME OVER",
            True,
            (255, 80, 80)
        )

        score_text = self.font.render(
            f"Final Score: {self.value}",
            True,
            (255, 255, 255)
        )

        screen.blit(
            title,
            (
                screen.get_width() // 2 - title.get_width() // 2,
                180
            )
        )

        screen.blit(
            score_text,
            (
                screen.get_width() // 2 - score_text.get_width() // 2,
                250
            )
        )