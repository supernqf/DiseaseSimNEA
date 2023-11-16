import pygame
import random
import time
class Particle:
    def __init__(self, x, y, color, screen_width, screen_height):
        self.x = x
        self.y = y
        self.state = "unaffected"
        self.color = color
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)
        self.screen_width = screen_width
        self.screen_height = screen_height
    def infect(self):
        self.state = "infected"
    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x < 0 or self.x > self.screen_width:
            self.vx *= -1
        if self.y < 0 or self.y > self.screen_height:
            self.vy *= -1
    def draw(self, screen):
        if self.state == "infected":
            color = (0, 255, 0)  # Set infected color to green (0, 255, 0)
        elif self.state == "dead":
            color = (0, 0, 0)  # Set dead color to black (0, 0, 0)
        else:
            color = self.color
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), 5)
    def check_collision(self, particles, chance_of_infection):
        if self.state == "unaffected":
            for particle in particles:
                if (self is not particle
                        and particle.state == "infected"
                        and self.collides(particle)
                        and random.random() < chance_of_infection):
                    self.infect()
                    break  # Break the loop once infected by one infected particle
    def collides(self, particle):
        dx = particle.x - self.x
        dy = particle.y - self.y
        distance = (dx ** 2 + dy ** 2) ** 0.5
        return distance < 20
