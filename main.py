import pygame
import random
from classes import Particle
NULL_COLOR = (128, 128, 128)
WHITE = (255, 255, 255)
INFECTED_COLOR = (0, 255, 0)
BLACK = (0, 0, 0)
if __name__ == "__main__":
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Disease Simulator")
    particles = []
    num_particles = 1000
    num_infected_particles = int(input("Enter the number of infected particles: "))
    num_null_particles = num_particles - num_infected_particles
    chance_of_infection = float(input("Enter the chance of infection (0-1): "))
    for _ in range(num_infected_particles):
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        overlaps = False
        for particle in particles:
            if abs(particle.x - x) < 20 and abs(particle.y - y) < 20:
                overlaps = True
                break
        if not overlaps:
            particles.append(Particle(x, y, INFECTED_COLOR))
    for _ in range(num_null_particles):
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        overlaps = False
        for particle in particles:
            if abs(particle.x - x) < 20 and abs(particle.y - y) < 20:
                overlaps = True
                break
        if not overlaps:
            particles.append(Particle(x, y, NULL_COLOR))

    for i in range(10):
        particles[i].infect()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(WHITE)

        for particle in particles:
            particle.move()
            particle.check_collision(particles, chance_of_infection)  # Pass the chance_of_infection parameter
            particle.draw(screen)
        pygame.display.flip()
        pygame.time.wait(100)
    pygame.quit()

