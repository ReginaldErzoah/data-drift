import pygame

class Player:
    def __init__(self):
        self.x = 380
        self.y = 420
        self.width = 50
        self.height = 50
        self.speed = 7

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        # boundaries
        self.x = max(0, min(self.x, 800 - self.width))

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 220, 120), (self.x, self.y, self.width, self.height))