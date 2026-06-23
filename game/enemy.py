import pygame
import random

class DataEnemy:
    def __init__(self):
        self.x = random.randint(40, 760)
        self.y = -20
        self.size = 35
        self.speed = random.randint(3, 6)

        self.type = random.choice(["NULL", "DUP", "OUTLIER", "BAD"])

        self.colors = {
            "NULL": (255, 80, 80),
            "DUP": (255, 170, 0),
            "OUTLIER": (180, 0, 255),
            "BAD": (255, 255, 0)
        }

    def update(self):
        self.y += self.speed

    def draw(self, screen):
        color = self.colors[self.type]
        pygame.draw.circle(screen, color, (self.x, self.y), self.size)

    def collides(self, player):
        return (
            self.x < player.x + player.width and
            self.x + self.size > player.x and
            self.y < player.y + player.height and
            self.y + self.size > player.y
        )