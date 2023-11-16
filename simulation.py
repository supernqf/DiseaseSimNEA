import pygame 
import random
from classes import Particle
from validation import get_valid_integer
def start_disease_simulation(screen_width, screen_height, screen):
  NULL_COLOR = (128, 128, 128)
  INFECTED_COLOR = (0, 255, 0)
  WHITE = (255, 255, 255)
  particles = []
  num_particles = 1000
  num_infected_particles = get_valid_integer("Enter the number of infected particles: ")
  num_null_particles = num_particles - num_infected_particles
  chance_of_infection = float(input("Enter the chance of infection (0-1): "))
  for _ in range(num_infected_particles):
      x = random.randint(0, screen_width)
      y = random.randint(0, screen_height)
      overlaps = False
      for particle in particles:
          if abs(particle.x - x) < 20 and abs(particle.y - y) < 20:
              overlaps = True
              break
      if not overlaps:
          particles.append(Particle(x, y, INFECTED_COLOR, screen_width, screen_height))
  for _ in range(num_null_particles):
      x = random.randint(0, screen_width)
      y = random.randint(0, screen_height)
      overlaps = False
      for particle in particles:
          if abs(particle.x - x) < 20 and abs(particle.y - y) < 20:
              overlaps = True
              break
      if not overlaps:
          particles.append(Particle(x, y, NULL_COLOR, screen_width, screen_height))
  for i in range(10):
      particles[i].infect()
  sim_running = True
  while sim_running:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              sim_running = False
      screen.fill(WHITE)
      for particle in particles:
          particle.move()
          particle.check_collision(particles, chance_of_infection)  # Pass the chance_of_infection parameter
          particle.draw(screen)
      pygame.display.flip()
      pygame.time.wait(100)
