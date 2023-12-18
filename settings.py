import pygame


def particlesetup(screen):
    screen_width = 800
    screen_height = 600
    input_screen = pygame.display.set_mode((screen_width, screen_height))

    input_str_particles = ''
    font = pygame.font.Font(None, 26)
    prompt_particles = "Enter total particles of simulation:"
    color = (0, 255, 0)
    input_box_rect_particles = pygame.Rect(100, 100, 140, 32)
    tick_box_rect = pygame.Rect(100, 160, 30, 30)
    text_vaccinations_enabled = "Vaccinations Enabled"
    text_vaccinations_disabled = "Vaccinations Disabled"
    text_vaccinations_rect = pygame.Rect(150, 165, 180, 20)
    active = "particles"
    vaccines = False  # Flag to represent the state of vaccines
    tick_img = pygame.image.load('tick.png')  # Load tick image
    tick_img = pygame.transform.scale(tick_img, (tick_box_rect.width, tick_box_rect.height))  # Resize tick image
    ticked = False  # Flag to indicate if tick is displayed

    input_screen.fill((255, 255, 255))
    base_surface_particles = font.render(prompt_particles, True, color)
    input_screen.blit(base_surface_particles, (50, 50))
    pygame.draw.rect(input_screen, color, input_box_rect_particles, 2)
    pygame.draw.rect(input_screen, color, tick_box_rect, 2)

    # Display "Vaccinations Disabled" initially
    text_vaccinations_surface = font.render(text_vaccinations_disabled, True, color)
    input_screen.blit(text_vaccinations_surface, text_vaccinations_rect.topleft)

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
                        return value_particles # Return both values
                    except ValueError:
                        input_str_particles = ''
                        base_surface_particles = font.render(
                            prompt_particles + " (Please enter a valid integer)", True, color)
                elif event.key == pygame.K_BACKSPACE:
                    if active == "particles":
                        input_str_particles = input_str_particles[:-1]
                elif event.key in [pygame.K_MINUS, pygame.K_PERIOD]:
                    if active == "particles":
                        input_str_particles += event.unicode
                elif event.unicode.isdigit():
                    if active == "particles":
                        input_str_particles += event.unicode

                # Update the screen after text input
                input_screen.fill((255, 255, 255))
                input_screen.blit(base_surface_particles, (50, 50))
                text_surface_particles = font.render(input_str_particles, True, color)
                input_screen.blit(
                    text_surface_particles,
                    (input_box_rect_particles.x + 5, input_box_rect_particles.y + 5))
                pygame.draw.rect(input_screen, color, input_box_rect_particles, 2)

                # Always draw the tick box
                pygame.draw.rect(input_screen, color, tick_box_rect, 2)

                # Draw tick image inside the tick box if ticked is True
                if ticked:
                    input_screen.blit(tick_img, tick_box_rect.topleft)  # Draw tick image inside the box
                    text_vaccinations_surface = font.render(text_vaccinations_enabled, True, color)
                else:
                    text_vaccinations_surface = font.render(text_vaccinations_disabled, True, color)

                input_screen.blit(text_vaccinations_surface, text_vaccinations_rect.topleft)

                pygame.display.flip()
                pygame.time.wait(100)







