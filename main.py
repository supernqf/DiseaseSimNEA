import pygame
import random
from classes import *
from validation import *

pygame.init()
# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Nath's Disease Simulator")


def runsim():
  from simulation import start_disease_simulation
  # Define the colours used
  WHITE = (255, 255, 255)
  GREEN = (0, 255, 0)
  BLACK = (0, 0, 0)
  input_box_rect = pygame.Rect(50, 100, 140, 32)
  input_box_rect_integer = pygame.Rect(50, 100, 140, 32)
  input_box_rect_infection = pygame.Rect(50, 300, 140, 32)
  input_box_rect_death_rate = pygame.Rect(50, 500, 140, 32)
  

  # Define the button's dimensions and positions
  button_width = 200
  button_height = 50
  play_button_pos = (screen_width // 2 - button_width // 2, 200)
  settings_button_pos = (screen_width // 2 - button_width // 2, 300)
  # Set up the fontt
  font = pygame.font.Font(None, 26)
  # Game loop to keep it running
  running = True
  num_infected_particles = 0
  chance_of_infection = 0.0
  total_particles = 1000
  while running:
    for event in pygame.event.get():
      
      if event.type == pygame.QUIT:
        running = False
      mouse_x, mouse_y = pygame.mouse.get_pos()
      if event.type == pygame.MOUSEBUTTONDOWN:
        # Check if th e Play button is clicked
        if (play_button_pos[0] <= mouse_x <= play_button_pos[0] + button_width
            and play_button_pos[1] <= mouse_y <=
            play_button_pos[1] + button_height):
          num_infected_particles, chance_of_infection, death_rate = get_valid_inputs(
            screen, "Enter number of infected particles:",
            "Enter chance of infection (0-1):", "Enter death rate (0-1):",
            font, GREEN, input_box_rect_integer, input_box_rect_infection,
            input_box_rect_death_rate)
          start_disease_simulation(screen_width, screen_height, screen,
                                   num_infected_particles, chance_of_infection,
                                   death_rate, total_particles)
        # Check if Settings button is clicked
        elif (settings_button_pos[0] <= mouse_x <=
              settings_button_pos[0] + button_width and settings_button_pos[1]
              <= mouse_y <= settings_button_pos[1] + button_height):
          from settings import particlesetup
          total_particles = particlesetup(screen)
    # Clear the screen
    screen.fill(WHITE)
    background = pygame.image.load("backky.png")
    
    screen.blit(background, (0, 0 ))
    logo_img = pygame.image.load('logo.png')
    logo_img = pygame.transform.scale(logo_img, (750, 300))
    screen.blit(logo_img, (screen_width / 2 - 350 , screen_height - 650))
    # Draw the Play button
    pygame.draw.rect(screen, GREEN,
                     (*play_button_pos, button_width, button_height))
    play_text = font.render('Play', True, BLACK)
    screen.blit(
      play_text,
      (play_button_pos[0] + (button_width - play_text.get_width()) // 2,
       play_button_pos[1] + (button_height - play_text.get_height()) // 2))
    # Draw the Settings button
    pygame.draw.rect(screen, GREEN,
                     (*settings_button_pos, button_width, button_height))
    settings_text = font.render('Settings', True, BLACK)
    screen.blit(settings_text,
                (settings_button_pos[0] +
                 (button_width - settings_text.get_width()) // 2,
                 settings_button_pos[1] +
                 (button_height - settings_text.get_height()) // 2))
    # Update the display to ensure it is accurate.
    pygame.display.flip()
    # Cap the frame rate
    pygame.time.Clock().tick(60)
  pygame.quit()




