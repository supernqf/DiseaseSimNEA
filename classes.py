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
        self.time_since_infection = 0  # Track time since infection
    def infect(self):
        self.state = "infected"
        self.time_since_infection = pygame.time.get_ticks()  # Record the time of infection
    def die(self):
        self.state = "dead"
        self.vx = 0
        self.vy = 0
    def move(self):
        if self.state != "dead":  # Dead particles don't move
            self.x += self.vx
            self.y += self.vy
            if self.x < 0 or self.x > self.screen_width:
                self.vx *= -1
            if self.y < 0 or self.y > self.screen_height:
                self.vy *= -1
    def draw(self, screen):
        if self.state == "infected":
            color = (0, 255, 0)  # Set infected color to green
        elif self.state == "dead":
            color = (0, 0, 0)  # Set dead color to black
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
    def check_death(self, death_rate):
        # Check if enough time has passed (1 second) to consider changing the state to dead
        if self.state == "infected" and (pygame.time.get_ticks() - self.time_since_infection) >= 1000:
            if random.random() < death_rate:
                self.die()
            self.time_since_infection += 1000  # Reset the time since the last death check
    def collides(self, particle):
        dx = particle.x - self.x
        dy = particle.y - self.y
        distance = (dx ** 2 + dy ** 2) ** 0.5
        return distance < 20
