import pygame, sys, time, random
from pygame.locals import *

pygame.init()
windowSurface = pygame.display.set_mode((400,300))
pygame.display.set_caption("Schrodingers Cat")
done = False

windowSurface = pygame.display.set_mode((500, 400), 0, 32)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

x=30
y=30


clock = pygame.time.Clock()

#main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= 5
    if pressed[pygame.K_DOWN]:
        y += 5
    if pressed[pygame.K_LEFT]:
        x -= 5
    if pressed[pygame.K_RIGHT]:
        x += 5

    windowSurface.fill(WHITE)
    pygame.draw.circle(windowSurface, BLUE, (300, 50) , 15, 0)
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
