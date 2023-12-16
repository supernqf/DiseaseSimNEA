import pygame
import time
pygame.init()
# Set up the display
screen_width = 800
screen_height = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 32)
screen = pygame.display.set_mode((screen_width, screen_height))
def show_loading_screen():
    screen.fill(WHITE)
    text = FONT.render("Loading...", True, BLACK)
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    time.sleep(2)

# Function to display the "Welcome!" message for 3 seconds
def show_welcome_screen():
    screen.fill(WHITE)
    text = FONT.render("Welcome!", True, BLACK)
    text_rect = text.get_rect(center=(screen_height// 2, screen_height // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    time.sleep(3)  # Display for 3 seconds