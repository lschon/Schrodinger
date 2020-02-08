import pygame

pygame.init()

display_width=800
display_height=600
cat_width=120
cat_height=100
quartercircle_width=60
quartercircle_height=60
xcat=30
ycat=30
vel=5
xrad=100
yrad=100
sizerad=50

clock = pygame.time.Clock()

windowSurface = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Schrodingers Cat: Wanted Dead or Alive')

cat = pygame.image.load('pusspuss.png')
cat = pygame.transform.scale(cat, (cat_width, cat_height))
corner = pygame.image.load('radiationshooter.png')
corner = pygame.transform.scale(corner, (quartercircle_width, quartercircle_height))

quartercircle1 = corner
quartercircle1 = pygame.transform.rotate(quartercircle1, 270)

quartercircle2 = corner
quartercircle2 = pygame.transform.rotate(quartercircle2, 180)

quartercircle3 = corner
quartercircle3 = pygame.transform.rotate(quartercircle3, 0)

quartercircle4 = corner
quartercircle4 = pygame.transform.rotate(quartercircle4, 90)

done = False



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Radiation:

    def __init__(self, x, y, size):
        self.x=x
        self.y=y
        self.size=size
        self.colour=RED
        self.thickness=2

    def display(self):
        pygame.draw.circle(windowSurface, self.colour, (self.x, self.y), self.size, self.thickness)

radiation=Radiation(xrad, yrad, sizerad)

#main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and ycat > 0:
        ycat -= vel
    if pressed[pygame.K_DOWN] and ycat < display_height - cat_height:
        ycat += vel
    if pressed[pygame.K_LEFT] and xcat > 0:
        xcat -= vel
    if pressed[pygame.K_RIGHT] and xcat < display_width - cat_width:
        xcat += vel
    if pressed[pygame.K_a]:
        cat = pygame.image.load('alivepussy2.png')
        cat = pygame.transform.scale(cat, (cat_width, cat_height))
    if pressed[pygame.K_d]:
        cat = pygame.image.load('boned-Pussy.png')
        cat = pygame.transform.scale(cat, (cat_width, cat_height))
    if pressed[pygame.K_s]:
        cat = pygame.image.load('cat.png')
        cat = pygame.transform.scale(cat, (cat_width, cat_height))


    windowSurface.fill(WHITE)
    windowSurface.blit(cat, (xcat,ycat))
    windowSurface.blit(quartercircle1, (0,0))
    windowSurface.blit(quartercircle2, (display_width-quartercircle_width, 0))
    windowSurface.blit(quartercircle3, (0,display_height-quartercircle_height))
    windowSurface.blit(quartercircle4, (display_width-quartercircle_width, display_height-quartercircle_height))
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
