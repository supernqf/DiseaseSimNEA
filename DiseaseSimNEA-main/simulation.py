import pygame
import random
from classes import *  # Importing classes from a file named 'classes'
from validation import *  # Importing something from a file named 'validation'


# Function to start the disease simulation
def start_disease_simulation(screen_width, screen_height, screen,
                             num_infected_particles, chance_of_infection,
                             death_rate, total_particles):

  # Setting up colors and other variables
  NULL_COLOR = (128, 128, 128)
  INFECTED_COLOR = (0, 255, 0)
  WHITE = (255, 255, 255)
  BLACK = (0, 0, 0)
  BLUE = (173, 216, 230)
  survival_rate = 1 - death_rate
  particles = []
  num_particles = int(total_particles)
  num_null_particles = num_particles - num_infected_particles
  font = pygame.font.Font(None, 24)

  # Creating infected and null particles
  # Randomly placing them on the screen without overlapping
  # Also, infecting 'num_infected_particles' initially
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

  # Infecting the initially infected particles
  for i in range(num_infected_particles):
    particles[i].infect()

  # Loading images and setting up simulation controls
  pause_img = pygame.image.load('pause.png')
  pause_img = pygame.transform.scale(pause_img, (50, 50))
  play_img = pygame.image.load('play.png')
  play_img = pygame.transform.scale(play_img, (50, 50))
  sim_running = True
  paused = False

  # Storing last positions of particles
  last_positions = []
  # Adding UI elements
  pause_img = pygame.image.load('pause.png')
  pause_img = pygame.transform.scale(pause_img, (35, 35))
  infectpen_img = pygame.image.load('infectpen.png')
  infectpen_img = pygame.transform.scale(infectpen_img, (35, 35))
  nullpen_img = pygame.image.load('nullpen.png') 
  nullpen_img = pygame.transform.scale(nullpen_img, (35, 35))
  drawing_modei = False
  drawing_moden = False
  speed = 100
  speedup_button = pygame.image.load('speed.png')
  speedup_button = pygame.transform.scale(speedup_button, (35, 35))
  speeddown_button = pygame.transform.flip(speedup_button, True, False)

  # Function to draw an infected particle on mouse click
  def draw_iparticle(mouse_x, mouse_y):
    new_particle = Particle(mouse_x, mouse_y, INFECTED_COLOR, screen_width,
                            screen_height)
    new_particle.infect()
    for particle in particles:
      if particle.state == "infected" and new_particle.collides(particle):
        new_particle.infect()
    particles.append(new_particle)
    # Check for collisions only once
    
    
  
  # Function to draw a null particle on mouse click
  def draw_nparticle(mouse_x, mouse_y):
    new_particle = Particle(mouse_x, mouse_y, NULL_COLOR, screen_width, screen_height)
    for particle in particles:
      if particle.state == "infected" and new_particle.collides(particle):
          new_particle.infect()
    particles.append(new_particle)

  # Main simulation loop
  while sim_running:
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          mouse_pos = pygame.mouse.get_pos()
          infectpen_rect = infectpen_img.get_rect(topleft=(screen_width / 2 + 100, 0))
          nullpen_rect = nullpen_img.get_rect(topleft=(screen_width / 2 + 125, 0))
          pause_button_rect = pause_img.get_rect(topleft=(screen_width / 2 - 25, 0))
          if infectpen_rect.collidepoint(mouse_pos):
            drawing_modei = not drawing_modei
            drawing_moden = False
          if nullpen_rect.collidepoint(mouse_pos):
            drawing_moden = not drawing_moden
            drawing_modei = False
          if drawing_modei:
            draw_iparticle(*mouse_pos)
          if drawing_moden:
            draw_nparticle(*mouse_pos)
           
          elif pause_button_rect.collidepoint(mouse_pos):
            paused = not paused
            if paused:
              screen.blit(play_img, (screen_width / 2 - 25, 0))
          if speedup_button.get_rect(topleft=(screen_width / 2 + 55,
                                              0)).collidepoint(mouse_pos):
            speed -= 1
           
          elif speeddown_button.get_rect(topleft=(screen_width / 2 - 105,
                                                  0)).collidepoint(mouse_pos):
            speed += 1
            
    # Updating the screen
    pygame.display.flip()
    screen.fill(WHITE)  # Setting background color

    # Displaying infected and dead counts
    infected_text = font.render("Infected: " + str(Particle.infection_count),
                                True, BLACK)
    screen.blit(infected_text, (10, 10))
    dead_text = font.render("Dead: " + str(Particle.death_count), True, BLACK)
    screen.blit(dead_text, (10, 30))

    # Updating and drawing particles
    for particle in particles:
      if not paused:
        particle.move()
        particle.check_interaction(particles, chance_of_infection)
        particle.check_collision(particles, chance_of_infection)
        particle.check_status(death_rate, survival_rate)
      particle.draw(screen)
      last_positions.append((particle.x, particle.y))

    # Displaying stats and UI elements
    infected_text = font.render("Infected: " + str(Particle.infection_count),True, BLACK)
    screen.blit(infected_text, (10, 10))
    dead_text = font.render("Dead: " + str(Particle.death_count), True, BLACK)
    screen.blit(dead_text, (10, 30))
    screen.blit(infectpen_img, (screen_width / 2 + 100, 0))
    screen.blit(nullpen_img, (screen_width / 2 + 125, 0))
    screen.blit(pause_img, (screen_width / 2 - 25, 0))
    screen.blit(speedup_button, (screen_width / 2 + 55, 0))
    screen.blit(speeddown_button, (screen_width / 2 - 105, 0))

    # Showing simulation completion message and options to restart
    if Particle.infection_count == 0:
      screen.fill(WHITE)
      result_text = font.render("Simulation Complete", True, BLACK)
      result_deaths = font.render("Deaths: " + str(Particle.death_count) + " out of " + str(num_particles), True, BLACK)
      screen.blit(result_text,(screen_width / 2 - 100, screen_height / 2 - 50))
      screen.blit(result_deaths, (screen_width / 2 - 100, screen_height / 2))
      result_survived = font.render("Survived: " + str(Particle.survival_count) + " out of " +str(num_particles), True, BLACK)
      screen.blit(result_survived,(screen_width / 2 - 100, screen_height / 2 + 50))
      retry_img = pygame.image.load('retry.png')
      retry_img = pygame.transform.scale(retry_img, (100, 100))
      screen.blit(retry_img, (screen_width / 2 - 25, screen_height / 2 + 100))
      mouse_x, mouse_y = pygame.mouse.get_pos()
      if (screen_width / 2 - 25 <= mouse_x <= screen_width / 2 + 150
          and screen_height / 2 + 75 <= mouse_y <= screen_height / 2 + 100):
        from main import runsim  # Importing a function from a file named 'main'
        runsim()
    pygame.display.flip()
    pygame.time.wait(speed)  # Controlling the simulation speed

