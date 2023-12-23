import pygame
import sqlite3
import time

# Initialize Pygame
pygame.init()

# Constants
screen_width = 800
screen_height = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PGREEN = (162, 255, 178)
FONT = pygame.font.Font(None, 32)

# Create a window
screen = pygame.display.set_mode((screen_width, screen_height))


# Function to create a database and table for storing user information
def create_database():
  conn = sqlite3.connect('users.db')
  cursor = conn.cursor()

  # Create table if it doesn't exist
  cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
  conn.commit()
  conn.close()


# Function to register a new user
def register(username, password):
  connect = sqlite3.connect('users.db')
  cursor = connect.cursor()

  # Check if the username already exists
  cursor.execute("SELECT * FROM users WHERE username = ?", (username, ))
  existing_user = cursor.fetchone()

  if existing_user:
    connect.close()
    return "Username already exists. Please choose a different username."
  else:
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                   (username, password))
    connect.commit()
    connect.close()
    from vanity import show_loading_screen
    from vanity import show_welcome_screen
    show_loading_screen()
    show_welcome_screen()
    from main import runsim
    runsim(
    )  # Execute runsim() only when a new user is registered successfully
    return f"User '{username}' registered successfully."


# Function to log in a user
def login(username, password):
  conn = sqlite3.connect('users.db')
  cursor = conn.cursor()

  cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?",
                 (username, password))
  user = cursor.fetchone()

  if user:
    conn.close()
    return f"Welcome, {username}! Login successful."
  else:
    conn.close()
    return "Invalid username or password. Please try again."


# Function to simulate something after successful registration/login


# Main function for handling GUI
def main():
  create_database()

  input_username = ''
  input_password = ''
  feedback_text = ''

  while True:
    screen.fill(PGREEN)

    mouse_pos = pygame.mouse.get_pos()

    username_box = pygame.Rect(50, 50, 300, 50)
    password_box = pygame.Rect(50, 150, 300, 50)
    register_button_rect = pygame.Rect(50, 200, 100, 50)
    login_button_rect = pygame.Rect(250, 200, 100, 50)

    username_active = username_box.collidepoint(mouse_pos)
    password_active = password_box.collidepoint(mouse_pos)
    register_active = register_button_rect.collidepoint(mouse_pos)
    login_active = login_button_rect.collidepoint(mouse_pos)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

      if event.type == pygame.MOUSEBUTTONDOWN:
        if username_active:
          active_input = 'username'
        elif password_active:
          active_input = 'password'
        elif register_active:
          if input_username != '' and input_password != '':
            feedback_text = register(input_username, input_password)

        elif login_active:
          if input_username != '' and input_password != '':
            feedback_text = login(input_username, input_password)
            if feedback_text.startswith("Welcome"):
              from vanity import show_loading_screen
              from vanity import show_welcome_screen
              show_loading_screen()
              show_welcome_screen()
              from main import runsim
              runsim()

      if event.type == pygame.KEYDOWN:
        if active_input == 'username':
          if event.key == pygame.K_BACKSPACE:
            input_username = input_username[:-1]
          elif event.key != pygame.K_RETURN:
            input_username += event.unicode
        elif active_input == 'password':
          if event.key == pygame.K_BACKSPACE:
            input_password = input_password[:-1]
          elif event.key != pygame.K_RETURN:
            input_password += event.unicode

    # Render input boxes and buttons
    pygame.draw.rect(screen, (0, 100, 0), username_box, 2 if username_active else 1)
    pygame.draw.rect(screen, (0, 100, 0), password_box, 2 if password_active else 1)
    pygame.draw.rect(screen, (0, 100, 0), register_button_rect, 2 if register_active else 1)
    pygame.draw.rect(screen, (0, 100, 0), login_button_rect, 2 if login_active else 1)

    username_text = FONT.render("Username: " + input_username, True, BLACK)
    password_text = FONT.render("Password: " + "*" * len(input_password), True,
                                BLACK)
    register_text = FONT.render("Register", True, BLACK)
    login_text = FONT.render("Login", True, BLACK)
    feedback = FONT.render(feedback_text, True, BLACK)

    screen.blit(username_text, (60, 60))
    screen.blit(password_text, (60, 160))
    screen.blit(register_text, (60, 210))
    screen.blit(login_text, (270, 210))
    screen.blit(feedback, (50, 250))
    logo_img = pygame.image.load('logo.png')
    logo_img = pygame.transform.scale(logo_img, (750, 400))
    screen.blit(logo_img, (screen_width / 2 - 350, screen_height - 300))
    orangeman = pygame.image.load('orangeman.png')
    orangeman = pygame.transform.scale(orangeman, (70, 70))
    screen.blit(orangeman, (screen_width / 2 - 100 , screen_height / 2))
    greenman = pygame.image.load('greenman.png')
    greenman = pygame.transform.scale(greenman, (70, 70))
    screen.blit(greenman, (screen_width / 2 , screen_height / 2 - 50))
    hairy = pygame.image.load('hairy.png')
    hairy = pygame.transform.scale(hairy, (70, 70))
    screen.blit(hairy, (screen_width / 2 , screen_height / 2))
    squid = pygame.image.load('squid.png')
    squid = pygame.transform.scale(squid, (70, 70))
    screen.blit(squid, (screen_width / 2 - 100 , screen_height / 2 + 100))

    pygame.display.flip()


# Run the main function
if __name__ == '__main__':
  main()

