import pygame, sys, time, random
from pygame.locals import *

pygame.init()

display_width=500
display_height=500
cat_width=50
cat_height=50
quartercircle_width=20
quartercircle_height=20

clock = pygame.time.Clock()

windowSurface = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Schrodingers Cat')

cat = pygame.image.load('cat.png')
cat = pygame.transform.scale(cat, (cat_width, cat_height))
quartercircle = pygame.image.load('quartercircle.jpg')
quartercircle = pygame.image.load(quartercircle, (quartercircle_width, quartercircle_height))
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
    if pressed[pygame.K_UP] and y > 0:
        y -= vel
    if pressed[pygame.K_DOWN] and y < display_height - cat_height:
        y += vel
    if pressed[pygame.K_LEFT] and x > 0:
        x -= vel
    if pressed[pygame.K_RIGHT] and x < display_width - cat_width:
        x += vel

    windowSurface.fill(WHITE)
    windowSurface.blit(cat, (x,y))
    windowSurface.blit(quartercircle, (0,0))
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
