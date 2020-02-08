import pygame, sys, time, random
from pygame.locals import *

pygame.init()
windowSurface = pygame.display.set_mode((500,500), 0, 32)
pygame.display.set_caption("Schrodingers Cat")
done = False



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

x=30
y=30
radius=15
vel=5

clock = pygame.time.Clock()

#main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y > radius:
        y -= vel
    if pressed[pygame.K_DOWN] and y < 500 - radius:
        y += vel
    if pressed[pygame.K_LEFT] and x > radius:
        x -= vel
    if pressed[pygame.K_RIGHT] and x < 500 - radius:
        x += vel

    windowSurface.fill(WHITE)
    pygame.draw.circle(windowSurface, BLUE, (x, y), radius, 0)
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
