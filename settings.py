import pygame


def setup(screen):
  screen_width = 800
  screen_height = 600
  input_screen = pygame.display.set_mode((screen_width, screen_height))

  input_str_particles = ''
  font = pygame.font.Font(None, 26)
  prompt_particles = "Enter total particles of simulation:"
  color = (0, 255, 0)
  input_box_rect_particles = pygame.Rect(50, 100, 140, 32)
  active = "particles"
  input_screen.fill((255, 255, 255))
  base_surface_particles = font.render(prompt_particles, True, color)
  input_screen.blit(base_surface_particles, (50, 150))
  pygame.draw.rect(input_screen, color, input_box_rect_particles, 2)
  pygame.display.flip()
  while True:

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        raise SystemExit
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN and active == "particles":
          try:
            value_particles = int(input_str_particles)
            return value_particles
          except ValueError:
            input_str_particles = ''
            base_surface_particles = font.render(
              prompt_particles + " (Please enter a valid integer)", True,
              color)
        elif event.key == pygame.K_BACKSPACE:
          if active == "particles":
            input_str_particles = input_str_particles[:-1]
        elif event.key in [pygame.K_MINUS, pygame.K_PERIOD]:
          if active == "particles":
            input_str_particles += event.unicode
        elif event.unicode.isdigit():
          if active == "particles":
            input_str_particles += event.unicode
        input_screen.fill((255, 255, 255))
        input_screen.blit(base_surface_particles, (50, 150))
        text_surface_particles = font.render(input_str_particles, True, color)
        input_screen.blit(
          text_surface_particles,
          (input_box_rect_particles.x + 5, input_box_rect_particles.y + 5))
        pygame.draw.rect(input_screen, color, input_box_rect_particles, 2)
        pygame.display.flip()
        pygame.time.wait(100)
