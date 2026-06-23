import pygame

class Score:
    def __init__(self):
        self.value = 0
        self.font = pygame.font.SysFont("Arial", 24)

    def add_survival(self):
        self.value += 1

    def draw(self, screen):
        text = self.font.render(f"Score: {self.value}", True, (255, 255, 255))
        screen.blit(text, (10, 10))