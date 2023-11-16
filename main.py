import pygame 
import random
from classes import Particle
from validation import get_valid_integer
from simulation import start_disease_simulation
# Initialize pygame
pygame.init()
# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Menu")
# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
# Define button dimensions and positions
button_width = 200
button_height = 50
play_button_pos = (screen_width // 2 - button_width // 2, 200)
settings_button_pos = (screen_width // 2 - button_width // 2, 300)
# Set up the font
font = pygame.font.Font(None, 36)
# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if Play button is clicked
            if (play_button_pos[0] <= mouse_x <= play_button_pos[0] + button_width and
                    play_button_pos[1] <= mouse_y <= play_button_pos[1] + button_height):
                start_disease_simulation(screen_width, screen_height, screen)  
            # Check if Settings button is clicked
            elif (settings_button_pos[0] <= mouse_x <= settings_button_pos[0] + button_width and
                  settings_button_pos[1] <= mouse_y <= settings_button_pos[1] + button_height):
                print("Settings button clicked") 
    # Clear the screen
    screen.fill(WHITE)
    # Draw Play button
    pygame.draw.rect(screen, GREEN, (*play_button_pos, button_width, button_height))
    play_text = font.render('Play', True, BLACK)
    screen.blit(play_text, (play_button_pos[0] + (button_width - play_text.get_width()) // 2,
                            play_button_pos[1] + (button_height - play_text.get_height()) // 2))
    # Draw Settings button
    pygame.draw.rect(screen, GREEN, (*settings_button_pos, button_width, button_height))
    settings_text = font.render('Settings', True, BLACK)
    screen.blit(settings_text, (settings_button_pos[0] + (button_width - settings_text.get_width()) // 2,
                                settings_button_pos[1] + (button_height - settings_text.get_height()) // 2))
    # Update the display
    pygame.display.flip()
    # Cap the frame rate
    pygame.time.Clock().tick(60)
pygame.quit()
