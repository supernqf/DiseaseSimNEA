import pygame
import random
import time
class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.state = "unaffected"
        self.color = color
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)

    def infect(self):
        self.state = "infected"

    def move(self, sim_speed):
        dt = pygame.time.Clock().tick(60) / 1000  
        self.x += self.vx * sim_speed * dt
        self.y += self.vy * sim_speed * dt

    def draw(self, screen):
        if self.state == "infected":
            color = self.color
        elif self.state == "dead":
            color = (0, 0, 0)
        else:
            color = (128, 128, 128)
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), 5)
