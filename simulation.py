import pygame
import random
from classes import *
from validation import *



def start_disease_simulation(screen_width, screen_height, screen,
                             num_infected_particles, chance_of_infection,
                             death_rate, total_particles):

  NULL_COLOR = (128, 128, 128)
  INFECTED_COLOR = (0, 255, 0)
  WHITE = (255, 255, 255)
  BLACK = (0, 0, 0)
  BLUE = (173, 216, 230)
  survival_rate = 1 - death_rate
  particles = []
  num_particles = total_particles
  num_null_particles = num_particles - num_infected_particles
  font = pygame.font.Font(None, 24)
  for _ in range(num_infected_particles):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    overlaps = False
    for particle in particles:
      if abs(particle.x - x) < 1 and abs(particle.y - y) < 1:
        overlaps = True
        break
    if not overlaps:
      particles.append(
        Particle(x, y, INFECTED_COLOR, screen_width, screen_height))
  for _ in range(num_particles):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    overlaps = False
    for particle in particles:
      if abs(particle.x - x) < 20 and abs(particle.y - y) < 20:
        overlaps = True
        break
    if not overlaps:
      particles.append(Particle(x, y, NULL_COLOR, screen_width, screen_height))
  for i in range(num_infected_particles):
    particles[i].infect()

  pause_img = pygame.image.load('pause.png')
  pause_img = pygame.transform.scale(pause_img, (50, 50))
  play_img = pygame.image.load('play.png')
  play_img = pygame.transform.scale(play_img, (50, 50))
  sim_running = True
  paused = False
  # Main simulation loop
  last_positions = []  # list to store the last positions of particles
  pause_img = pygame.image.load('pause.png')
  pause_img = pygame.transform.scale(pause_img, (50, 50))
  play_img = pygame.image.load('play.png')
  play_img = pygame.transform.scale(play_img, (50, 50))
  # Main simulation loop
  while sim_running:
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          mouse_pos = pygame.mouse.get_pos()
          pause_button_rect = pause_img.get_rect(topleft=(screen_width / 2 -
                                                          25, 0))
          if pause_button_rect.collidepoint(mouse_pos):
            paused = not paused
            if paused:
              screen.blit(
                play_img,
                (screen_width / 2 - 25,
                 0))  # Change the pause image to play image while paused
            else:
              screen.blit(pause_img, (
                screen_width / 2 - 25,
                0))  # Change the play image back to pause image while unpaused
    # drawing the number of infected and dead particles in the top left

    screen.fill(WHITE)
    infected_text = font.render("Infected: " + str(Particle.infection_count),
                                True, BLACK)
    screen.blit(infected_text, (10, 10))
    dead_text = font.render("Dead: " + str(Particle.death_count), True, BLACK)
    screen.blit(dead_text, (10, 30))
    for particle in particles:
      if not paused:  # Only update and draw particles if not paused
        particle.move()
        particle.check_collision(particles, chance_of_infection)
        particle.check_status(death_rate, survival_rate)
      particle.draw(screen)
      last_positions.append(
        (particle.x, particle.y))  # Store the last positions of particles
    # Display the pause button at the top middle of the screen

    infected_text = font.render("Infected: " + str(Particle.infection_count),
                                True, BLACK)
    screen.blit(infected_text, (10, 10))
    dead_text = font.render("Dead: " + str(Particle.death_count), True, BLACK)
    screen.blit(dead_text, (10, 30))

    screen.blit(pause_img, (screen_width / 2 - 25, 0))
    if Particle.infection_count == 0:
      screen.fill(WHITE)
      result_text = font.render("Simulation Complete", True, BLACK)
      result_deaths = font.render(
        "Deaths: " + str(Particle.death_count) + " out of " + str(num_particles), True, BLACK)
      screen.blit(result_text,
                  (screen_width / 2 - 100, screen_height / 2 - 50))
      screen.blit(result_deaths, (screen_width / 2 - 100, screen_height / 2))
      result_survived = font.render(
        "Survived: " + str(Particle.survival_count) + " out of " + str(num_particles),  True, BLACK)
      screen.blit(result_survived, (screen_width / 2 - 100, screen_height / 2 + 50))
      
      retry_img = pygame.image.load('retry.png')
      retry_img = pygame.transform.scale(retry_img, (100, 100))
      screen.blit(retry_img, (screen_width / 2 - 25, screen_height / 2 + 100))
      mouse_x, mouse_y = pygame.mouse.get_pos()
      if (screen_width / 2 - 25 <= mouse_x <= screen_width / 2 + 25
          and screen_height / 2 + 75 <= mouse_y <= screen_height / 2 + 100):
        from main import runsim
        runsim()

    pygame.display.flip()
    pygame.time.wait(100)


