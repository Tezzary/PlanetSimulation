import math
from time import sleep
import pygame

class Planet :
    def __init__(self, name, mass, velocity, position, radius, color) :
        self.name = name
        self.mass = mass
        self.velocity = velocity
        self.position = position
        self.radius = radius
        self.color = color

    def calculatePull (self, planets) :
        totalAppliedForce = [0, 0]
        for planet in planets :
            if planet == self : continue
            deltaX, deltaY = planet.position[0] - self.position[0], planet.position[1] - self.position[1]
            distance = math.sqrt(deltaX * deltaX + deltaY * deltaY)
            force = G * self.mass * planet.mass / (distance * distance)
            theta = math.atan2(deltaY, deltaX)
            pullY = math.sin(theta) * force
            pullX = math.cos(theta) * force
            totalAppliedForce[0] += pullX / self.mass
            totalAppliedForce[1] += pullY / self.mass

        self.velocity[0] += totalAppliedForce[0]
        self.velocity[1] += totalAppliedForce[1]

    def applyVelocity(self, timeStep) :
        self.position[0] += self.velocity[0] * timeStep
        self.position[1] += self.velocity[1] * timeStep

pygame.init()

size = width, height = 1000, 1000

surface = pygame.display.set_mode(size)

G = 6.67e-11

planets = []

planets.append(Planet("Sun", 1.99e+30, [0, 0], [0, 0], 20, (255, 255, 0)))
planets.append(Planet("Mercury", 3.29e+23, [0, 47.87], [46096000000 , 0], 3, (170, 170, 170)))
planets.append(Planet("Venus", 4.87e+24, [0, 35.0], [107500000000 , 0], 5, (255, 150, 0)))
planets.append(Planet("Earth", 5.97e+24, [0, 29.78], [150080000000, 0], 5, (0, 255, 255)))
planets.append(Planet("Mars", 6.42e+23, [0, 24.1], [228000000000, 0], 3, (255, 0, 0)))
planets.append(Planet("Jupiter", 1.898e+27, [0, 13.1], [778500000000, 0], 10, (255, 100, 100)))

zoom = 1

while True :
    surface.fill([0, 0, 0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.exit()
        if event.type == pygame.MOUSEWHEEL:
            if event.y == 1 :
                zoom -= 1
            else :
                zoom += 1
    if(zoom > 5) :
        zoom = 1
    if zoom < 1 :
        zoom = 5
    for planet in planets :
        planet.calculatePull(planets)
        planet.applyVelocity(1000000)
        pygame.draw.circle(surface, planet.color, (width / 2 + planet.position[0] / (1e+9 * zoom), height / 2 + planet.position[1] / (1e+9 * zoom)), planet.radius)
  

    pygame.display.update()
