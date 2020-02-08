import pygame, sys, time, random
from pygame.locals import *

pygame.init()

display_width=500
display_height=500

clock = pygame.time.Clock()

windowSurface = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Schrodingers Cat')

cat = pygame.image.load('cat.png')

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


#main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y > radius:
        y -= vel
    if pressed[pygame.K_DOWN] and y < display_height - radius:
        y += vel
    if pressed[pygame.K_LEFT] and x > radius:
        x -= vel
    if pressed[pygame.K_RIGHT] and x < display_width - radius:
        x += vel

    windowSurface.fill(WHITE)
    display_surface.blit(cat, (x,y))
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
