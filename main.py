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
    for _ in range(num_infected_particles):
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        overlaps = False
        for particle in particles:
            if abs(particle.x - x) < 10 and abs(particle.y - y) < 10:
                overlaps = True
                break
        if not overlaps:
            particles.append(Particle(x, y, INFECTED_COLOR))
    for _ in range(num_null_particles):
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        overlaps = False
        for particle in particles:
            if abs(particle.x - x) < 10 and abs(particle.y - y) < 10:
                overlaps = True
                break
        if not overlaps:
            particles.append(Particle(x, y, NULL_COLOR))
    sim_speed = float(input("Enter the simulation speed: "))
    for i in range(10):
        particles[i].infect()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(WHITE)
        for particle in particles:
            particle.move(sim_speed)
            particle.draw(screen)
            for other_particle in particles:
                if particle is not other_particle:
                    dx = other_particle.x - particle.x
                    dy = other_particle.y - particle.y
                    distance = (dx ** 2 + dy ** 2) ** 0.5
                    if distance < 10:
                        particle.vx = -particle.vx
                        particle.vy = -particle.vy
                        other_particle.vx = -other_particle.vx
                        other_particle.vy = -other_particle.vy
                        if particle.state == "infected" and other_particle.state != "infected":
                            other_particle.infect()
                        elif other_particle.state == "infected" and particle.state != "infected":
                            particle.infect()
        pygame.display.flip()
        pygame.time.wait(int(100 * sim_speed))
    pygame.quit()

