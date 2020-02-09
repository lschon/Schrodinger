import pygame
import random
from pygame.locals import *
import math 

pygame.init()
display_width=800
display_height=600
cat_width=150
cat_height=100
quartercircle_width=60
quartercircle_height=60
xcat=0.5*display_width-0.5*cat_width
ycat=0.5*display_height-0.5*cat_height
vel=5
xrad=100
yrad=100
sizerad=50
anglerad=random.randint(0,90)


clock = pygame.time.Clock()
#Setting up screen visuals
screen = pygame.display.set_mode((display_width,display_height))
w, h = pygame.display.get_surface().get_size()
pygame.display.set_caption('Schrodingers Cat: Wanted Dead or Alive')
bgs = pygame.image.load("background_box.jpg")
bgs = pygame.transform.scale(bgs, (w, h))
bga = pygame.image.load("background_box_alive.jpg")
bga = pygame.transform.scale(bga, (w, h))
bgd = pygame.image.load("background_box_dead.jpg")
bgd = pygame.transform.scale(bgd, (w, h))
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
GREY = (160,160,160)
YELLOW = (255, 255, 50)
background = bgs
rate = 60
speed_factor = 0.5
font = pygame.font.Font(None, 36)
#MAKING THE INSTRUCTION PAGE
display_instructions = True
instruction_page=1
while not done and display_instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            instruction_page += 1
            if instruction_page == 2:
                display_instructions = False

    if instruction_page == 1:
        screen.blit(background, (0, 0))

        text = font.render("Schrödinger's Cat: Wanted Dead or Alive", True, BLUE)
        screen.blit(text, [10,10])
        text = font.render("The objective of the game... survive!", True, BLUE)
        screen.blit(text, [10,40])
        text = font.render("You are Schrödinger's cat and you are both dead and alive,", True, BLUE)
        screen.blit(text, [10,100])
        text = font.render("a state called quantum superposition by scientists!", True, BLUE)
        screen.blit(text, [10,130])
        text = font.render("Utilise this unique property and flip between the two states,", True, BLUE)
        screen.blit(text, [10,160])
        text = font.render("in order to avoid the radioactive particles trying to harm you!", True, BLUE)
        screen.blit(text, [10,190])
        text = font.render("Press the A key to use your LIVING powers... speed!", True, WHITE)
        screen.blit(text, [10,250])
        text = font.render("Press the D key to use your DEATHLY powers... slowing!", True, BLACK)
        screen.blit(text, [10,280])
        text = font.render("Press the S key to return to your in-between alive/dead state.", True, RED)
        screen.blit(text, [10,310])
        text = font.render("Try to survive for as long as you can... good luck!", True, BLUE)
        screen.blit(text, [10,370])
        text = font.render("Click to continue", True, BLUE)
        screen.blit(text, [10,400])
    pygame.display.flip()

class Radiation:

    def __init__(self, x, y, size):
        self.x=x
        self.y=y
        self.size=size
        self.colour=RED
        self.thickness=2

    def display(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)

radiation=Radiation(xrad, yrad, sizerad)

def random_angle(x,y):
    anglerad=random.randint(x, y)
    anglerad *= math.pi/180
    return anglerad


#particle print function, make 1 for each particle
def particle(part_x, part_y, radius, colour):
    pygame.draw.circle(screen, colour, (part_x, part_y), radius)
    return part_x, part_y	


rad1_x = 0
rad1_y = 0

rad2_x = 0
rad2_y = display_height

rad3_x = display_width
rad3_y = 0

rad4_x = display_width
rad4_y = display_height

rad_speed1 = 2
rad_speed2 = 2
rad_speed3 = 2
rad_speed4 = 2

rad_width = 5
rad_traj1 = random_angle(90, 180)
rad_traj2 = random_angle(0, 90)
rad_traj3 = random_angle(180,270)
rad_traj4 = random_angle(270,360)

#timer
counter, text = 0, '0'
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('comicsansms', 60)
timer_clr=BLACK
game_over=False

#main game loop
while not done:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True


        if event.type == pygame.USEREVENT:
            counter += 1
            text = str(counter)

    screen.blit(background, (0, 0))
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
        background = bga
        vel = 8
        rate = 60
        timer_clr = BLACK

    if pressed[pygame.K_d]:
        cat = pygame.image.load('boned-Pussy.png')
        cat = pygame.transform.scale(cat, (cat_width, cat_height))
        background = bgd
        vel = 10
        rate = 30
        timer_clr = WHITE

    if pressed[pygame.K_s]:
        cat = pygame.image.load('pusspuss.png')
        cat = pygame.transform.scale(cat, (cat_width, cat_height))
        background = bgs
        vel = 5
        rate = 60
        timer_clr = BLACK


    #NEED IF STATEMENT for when particle hits cat and then the counter stops and the end screen appears with counter time where DONE = TRUE & Game_over = True


    screen.blit(background, (0, 0))
    screen.blit(cat, (xcat,ycat))
    screen.blit(quartercircle1, (0,0))
    screen.blit(quartercircle2, (display_width-quartercircle_width, 0))
    screen.blit(quartercircle3, (0,display_height-quartercircle_height))
    screen.blit(font.render(text, True, (timer_clr)), (0.85*display_width, 0.1*display_height))
    screen.blit(quartercircle4, (display_width-quartercircle_width, display_height-quartercircle_height))

    print(rad1_x)
    p1x, p1y = particle(rad1_x, rad1_y, rad_width, GREEN)
    p2x, p2y = particle(rad2_x, rad2_y, rad_width, GREEN)
    p3x, p3y = particle(rad3_x, rad3_y, rad_width, GREEN)
    p4x, p4y = particle(rad4_x, rad4_y, rad_width, GREEN)
    rad1_y += rad_speed1*math.cos(rad_traj1)
    rad1_x += rad_speed1*math.sin(rad_traj1)
    rad2_y += rad_speed2*math.cos(rad_traj2)
    rad2_x += rad_speed2*math.sin(rad_traj2)
    rad3_y += rad_speed3*math.cos(rad_traj3)
    rad3_x += rad_speed3*math.sin(rad_traj3)
    rad4_y += rad_speed4*math.cos(rad_traj4)
    rad4_x += rad_speed4*math.sin(rad_traj4)

    #speed factor reversing (with a negative) the particle trajectory and increasing speed
    if (p1x < 0 or p1x > display_width or p1y < 0 or p1y > display_height):
        rad_speed1 += speed_factor
        rad1_x = 0
        rad1_y = 0
        rad_traj1 = random_angle(90, 180)
    if (p2x < 0 or p2x > display_width or p2y < 0 or p2y > display_height):
        rad_speed2 += speed_factor
        rad2_x = 0
        rad2_y = display_height
        rad_traj2 = random_angle(90, 180)
    if (p3x < 0 or p3x > display_width or p3y < 0 or p3y > display_height):
        rad_speed3 += speed_factor
        rad3_x = display_width
        rad3_y = 0
        rad_traj3 = random_angle(90, 180)
    if (p4x < 0 or p4x > display_width or p4y < 0 or p4y > display_height):
        rad_speed4 += speed_factor
        rad4_x = display_width
        rad4_y = display_height
        rad_traj4 = random_angle(90, 180)
        pygame.display.update()
        pygame.display.flip()
        clock.tick(rate)
    
    #When the game ends, say that game_over=True
    '''if game_over=True:
            screen.blit(background, (0, 0))
            largeFont = pygame.font.SysFont(None, 80) # creates a font object
            score = largeFont.render('Time alive: '+ str(count)+ " seconds",1, BLUE)
            screen.blit(score, display_height/2)
            pygame.display.update()'''
