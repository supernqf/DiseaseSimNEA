import pygame
import time

pygame.init()

# Screen setup
screen_width = 800
screen_height = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 32)
screen = pygame.display.set_mode((screen_width, screen_height))


def show_loading_screen():
  # Show a loading message
  screen.fill(WHITE)
  text = FONT.render("Loading...", True, BLACK)
  text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
  pygame.display.flip()
  time.sleep(0)


def show_welcome_screen():
  # Show a 'Welcome!' message for a short while
  screen.fill(WHITE)
  text = FONT.render("Welcome!", True, BLACK)
  text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
  screen.blit(text, text_rect)  #
  pygame.display.flip()
  time.sleep(0)
