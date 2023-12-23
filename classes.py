import pygame
import random
import time
import validation


class Particle:

  def __init__(self, x, y, color, screen_width, screen_height):
    # Initialize Particle attributes
    self.x = x
    self.y = y
    self.state = "unaffected"
    self.color = color
    self.vx = random.uniform(-2, 2)  # Velocity in x-direction
    self.vy = random.uniform(-2, 2)  # Velocity in y-direction
    self.screen_width = screen_width
    self.screen_height = screen_height
    self.time_since_infection = 0
    self.infection_duration = 6000  # Time in milliseconds for infection to progress

  death_count = 0
  infection_count = 0
  survival_count = 0

  def infect(self):
    # Infect the particle if it's currently unaffected
    if self.state == "unaffected":
      Particle.infection_count += 1
    self.state = "infected"
    self.time_since_infection = pygame.time.get_ticks()

  def die(self):
    # Set particle state to 'dead'
    if self.state != "dead" and self.state != "survived":
      Particle.death_count += 1
      Particle.infection_count -= 1
    self.state = "dead"
    self.vx = 0
    self.vy = 0

  def survive(self):
    # Set particle state to 'survived'
    if self.state != "survived" and self.state != "dead":
      Particle.survival_count += 1
      Particle.infection_count -= 1
    self.state = "survived"
    self.vx = 0
    self.vy = 0

  def move(self):
    # Move the particle within screen boundaries
    if self.state != "dead":
      self.x += self.vx
      self.y += self.vy
      if self.x < 0 or self.x > self.screen_width:
        self.vx *= -1
      if self.y < 0 or self.y > self.screen_height:
        self.vy *= -1

  def draw(self, screen):
    # Draw the particle based on its state
    if self.state == "infected":
      color = (0, 255, 0)
    elif self.state == "dead":
      color = (0, 0, 0)
    elif self.state == "survived":
      color = (173, 216, 230)
    else:
      color = self.color
    pygame.draw.circle(screen, color, (int(self.x), int(self.y)), 5)

  def check_collision(self, particles, chance_of_infection):
    # Check collision with other particles for possible infection
    if self.state == "unaffected":
      for particle in particles:
        if self is not particle and particle.state == "infected" and self.collides(
            particle) and random.random() < chance_of_infection:
          self.infect()
          break

  def check_status(self, death_rate, survival_rate):
    # Check the status of an infected particle over time
    if self.state == "infected" and (
        pygame.time.get_ticks() -
        self.time_since_infection) >= self.infection_duration:
      if random.random() < death_rate:
        self.die()
      self.time_since_infection += 1000
      if death_rate != 1:
        if self.time_since_infection >= self.infection_duration * (
            1 / survival_rate) and death_rate != 0 and death_rate != 1:
          self.survive()
        if death_rate == 0 and self.time_since_infection >= self.infection_duration:
          self.survive()

  def collides(self, particle):
    # Check if the particle collides with another particle
    dx = particle.x - self.x
    dy = particle.y - self.y
    distance = (dx**2 + dy**2)**0.5
    return distance < 20

  def check_interaction(self, other_particles, chance_of_infection):
    # Check interaction with other particles for possible infection
    if self.state == "unaffected":
      for particle in other_particles:
        if self is not particle and particle.state == "infected" and self.collides(
            particle) and random.random() < chance_of_infection:
          self.infect()
          break

