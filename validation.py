import pygame
def displayboxes(screen, font, color):
  label_font = pygame.font.SysFont(None, 24)  # Font for the labels

  preset1 = pygame.Rect(600, 100, 150, 50)
  text1 = label_font.render("Ebola", True, color)

  preset2 = pygame.Rect(600, 250, 150, 50)
  text2 = label_font.render("Measles", True, color)

  preset3 = pygame.Rect(600, 400, 150, 50)
  text3 = label_font.render("Corona Virus", True, color)

  presetboxes = [(preset1, text1),
                (preset2, text2),
                (preset3, text3)]

  for box, text in presetboxes:
      pygame.draw.rect(screen, color, box, 2)
      screen.blit(text, (box.x + 10, box.y + 10))

  return presetboxes
def switch_active_box(active, input_boxes, mouse_pos):
  for index, box in enumerate(input_boxes):
    if box.collidepoint(mouse_pos):
        return index
  return active

  # Updated main function incorporating labeled box functionality
def get_valid_inputs(screen, prompt_integer, prompt_infection,
                    prompt_death_rate, font, color, input_box_rect_integer,
                    input_box_rect_infection, input_box_rect_death_rate):
  input_screen = pygame.display.set_mode((800, 600))
  input_str_integer = ''
  input_str_infection = ''
  input_str_death_rate = ''
  base_surface_integer = font.render(prompt_integer, True, color)
  base_surface_infection = font.render(prompt_infection, True, color)
  base_surface_death_rate = font.render(prompt_death_rate, True, color)
  active = "integer"

  input_screen.fill((0, 0, 0))
  input_screen.blit(base_surface_integer, (50, 150))
  pygame.draw.rect(input_screen, color, input_box_rect_integer, 2)
  input_screen.blit(base_surface_infection, (50, 350))
  pygame.draw.rect(input_screen, color, input_box_rect_infection, 2)
  input_screen.blit(base_surface_death_rate, (50, 550))
  pygame.draw.rect(input_screen, color, input_box_rect_death_rate, 2)

    # Display labeled boxes
  presetboxes = displayboxes(input_screen, font, color)
  pygame.display.flip()
  
  while True:
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    for box, _ in presetboxes:
      if box.collidepoint(mouse_pos):
          if click[0] == 1:  # Left mouse button clicked
              if box == presetboxes[0][0]:  # Placeholder values for Default 1
                  input_str_integer = '50'
                  input_str_infection = '0.5'
                  input_str_death_rate = '0.1'
              elif box == presetboxes[1][0]:  # Placeholder values for Default 2
                  input_str_integer = '100'
                  input_str_infection = '0.3'
                  input_str_death_rate = '0.05'
              elif box == presetboxes[2][0]:  # Placeholder values for Default 3
                  input_str_integer = '25'
                  input_str_infection = '0.7'
                  input_str_death_rate = '0.2'

    # Redraw input boxes with updated placeholder values
    input_screen.fill((0, 0, 0))
    input_screen.blit(base_surface_integer, (50, 150))
    text_surface_integer = font.render(input_str_integer, True, color)
    input_screen.blit(text_surface_integer, (input_box_rect_integer.x + 5, input_box_rect_integer.y + 5))
    pygame.draw.rect(input_screen, color, input_box_rect_integer, 2)

    input_screen.blit(base_surface_infection, (50, 350))
    text_surface_infection = font.render(input_str_infection, True, color)
    input_screen.blit(text_surface_infection, (input_box_rect_infection.x + 5, input_box_rect_infection.y + 5))
    pygame.draw.rect(input_screen, color, input_box_rect_infection, 2)

    input_screen.blit(base_surface_death_rate, (50, 550))
    text_surface_death_rate = font.render(input_str_death_rate, True, color)
    input_screen.blit(text_surface_death_rate, (input_box_rect_death_rate.x + 5, input_box_rect_death_rate.y + 5))
    pygame.draw.rect(input_screen, color, input_box_rect_death_rate, 2)

    # Redraw labeled boxes
    presetboxes = displayboxes(input_screen, font, color)

    pygame.display.flip()
    pygame.time.wait(100)
    if click[0] == 1:
      if input_box_rect_integer.collidepoint(mouse_pos):
          active = "integer"
      elif input_box_rect_infection.collidepoint(mouse_pos):
          active = "infection"
      elif input_box_rect_death_rate.collidepoint(mouse_pos):
          active = "death_rate"

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        raise SystemExit
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN and active == "integer":
          try:
            value_integer = int(input_str_integer)
            base_surface_integer = font.render(prompt_integer, True, color)
            active = "infection"
          except ValueError:
            input_str_integer = ''
            base_surface_integer = font.render(
              prompt_integer + " (Please enter a valid integer)", True, color)
        elif event.key == pygame.K_RETURN and active == "infection":
          try:
            value_infection = float(input_str_infection)
            if 0 <= value_infection <= 1:
              base_surface_infection = font.render(prompt_infection, True,
                                                   color)
              active = "death_rate"
            else:
              input_str_infection = ''
              base_surface_infection = font.render(
                prompt_infection + " (Please enter a value between 0 and 1)",
                True, color)
          except ValueError:
            input_str_infection = ''
            base_surface_infection = font.render(
              prompt_infection + " (Please enter a valid float)", True, color)
        elif event.key == pygame.K_RETURN and active == "death_rate":
          try:
            value_death_rate = float(input_str_death_rate)
            if 0 <= value_death_rate <= 1:
              return value_integer, value_infection, value_death_rate
            else:
              input_str_death_rate = ''
              base_surface_death_rate = font.render(
                prompt_death_rate + " (Please enter a value between 0 and 1)",
                True, color)
          except ValueError:
            input_str_death_rate = ''
            base_surface_death_rate = font.render(
              prompt_death_rate + " (Please enter a valid float)", True, color)
        elif event.key == pygame.K_BACKSPACE:
          if active == "integer":
            input_str_integer = input_str_integer[:-1]
          elif active == "infection":
            input_str_infection = input_str_infection[:-1]
          else:
            input_str_death_rate = input_str_death_rate[:-1]
        elif event.key in [pygame.K_MINUS, pygame.K_PERIOD]:
          if active == "infection" or active == "death_rate":
            if active == "infection":
              input_str_infection += event.unicode
            elif active == "death_rate":
              input_str_death_rate += event.unicode
        elif event.unicode.isdigit():
          if active == "integer":
            input_str_integer += event.unicode
          elif active == "infection":
            input_str_infection += event.unicode
          elif active == "death_rate":
            input_str_death_rate += event.unicode
          elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
          # Handle switching between input boxes by mouse click
            active = switch_active_box(active, [input_box_rect_integer,       input_box_rect_infection, input_box_rect_death_rate], mouse_pos)

          # Handle input for each input box
            if input_box_rect_integer.collidepoint(mouse_pos):
              active = "integer"
            elif input_box_rect_infection.collidepoint(mouse_pos):
              active = "infection"
            elif input_box_rect_death_rate.collidepoint(mouse_pos):
                active = "death_rate"
        input_screen.fill((0, 0, 0))
        input_screen.blit(base_surface_integer, (50, 150))
        text_surface_integer = font.render(input_str_integer, True, color)
        input_screen.blit(
          text_surface_integer,
          (input_box_rect_integer.x + 5, input_box_rect_integer.y + 5))
        pygame.draw.rect(input_screen, color, input_box_rect_integer, 2)
        input_screen.blit(base_surface_infection, (50, 350))
        text_surface_infection = font.render(input_str_infection, True, color)
        input_screen.blit(
          text_surface_infection,
          (input_box_rect_infection.x + 5, input_box_rect_infection.y + 5))
        pygame.draw.rect(input_screen, color, input_box_rect_infection, 2)
        input_screen.blit(base_surface_death_rate, (50, 550))
        text_surface_death_rate = font.render(input_str_death_rate, True,
                                              color)
        input_screen.blit(
          text_surface_death_rate,
          (input_box_rect_death_rate.x + 5, input_box_rect_death_rate.y + 5))
        pygame.draw.rect(input_screen, color, input_box_rect_death_rate, 2)
        pygame.display.flip()
        pygame.time.wait(100)


