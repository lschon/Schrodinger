import pygame
import random
from pygame.locals import *
import math 

pygame.init()
display_width=800
display_height=600
cat_width=100
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
rad_width = 20
rad_height = 20

clock = pygame.time.Clock()
#Setting up screen visuals
screen = pygame.display.set_mode((display_width,display_height))
w, h = pygame.display.get_surface().get_size()
pygame.display.set_caption('Schrodingers Cat: Wanted Dead or Alive')
bgs = pygame.image.load("background_box.jpg").convert()
bgs = pygame.transform.scale(bgs, (w, h))
bga = pygame.image.load("background_box_alive.jpg").convert()
bga = pygame.transform.scale(bga, (w, h))
bgd = pygame.image.load("background_box_dead.jpg").convert()
bgd = pygame.transform.scale(bgd, (w, h))
cat = pygame.image.load('pusspuss.png').convert_alpha()
cat = pygame.transform.scale(cat, (cat_width, cat_height))
corner = pygame.image.load('radiationshooter.png').convert_alpha()
corner = pygame.transform.scale(corner, (quartercircle_width, quartercircle_height))
quartercircle1 = corner
quartercircle1 = pygame.transform.rotate(quartercircle1, 270)
quartercircle2 = corner
quartercircle2 = pygame.transform.rotate(quartercircle2, 180)
quartercircle3 = corner
quartercircle3 = pygame.transform.rotate(quartercircle3, 0)
quartercircle4 = corner
quartercircle4 = pygame.transform.rotate(quartercircle4, 90)
alpha = pygame.image.load('alpha.png').convert_alpha()
alpha = pygame.transform.scale(alpha, (rad_width, rad_height))

done = False

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

GREY = (160,160,160)
YELLOW = (255, 255, 50)
background = bgs
rate = 30
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
        text = font.render("Press the S key to return to your superposition, alive/dead state.", True, RED)
        screen.blit(text, [10,310])
        text = font.render("Try to survive for as long as you can... good luck!", True, BLUE)
        screen.blit(text, [10,370])
        text = font.render("Click to continue", True, BLUE)
        screen.blit(text, [10,400])
    pygame.display.flip()

#def check_collision(x1, x2, x3, x4, y1, y2, y3, y4):


def random_angle(x,y):
    anglerad=random.randint(x, y)
    anglerad *= math.pi/180
    return anglerad

def particle(part_x, part_y, height, width, colour):
    pygame.draw.rect(screen, colour, (part_x, part_y, height, width))
    
rad1_x = 1
rad1_y = 1

rad2_x = display_width - 1
rad2_y = 1

rad3_x = 1
rad3_y = display_height - 1

rad4_x = display_width - 1
rad4_y = display_height - 1

rad_speed1 = 10
rad_speed2 = 10
rad_speed3 = 10
rad_speed4 = 10

rad_traj1 = random_angle(0, 90)
rad_traj2 = random_angle(270, 360)
rad_traj3 = random_angle(90,180)
rad_traj4 = random_angle(180,270)

#timer
counter, text = 0, '0'
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('comicsansms', 60)
timer_clr=BLACK
game_over=False

def check_collision(x1, y1, catx, caty, counter):
    global cat_width, cat_height
        #if ((catx - cat_width/2 <= x_vals[i] <= catx + cat_width/2) and (caty - cat_height/2 <= y_vals[i] <= caty + cat_height/2))
    if (x1 < (catx+cat_width)) and (x1 > (catx)) and (y1 < (caty+cat_height)) and (y1 > (caty)):
        return True
    else:
        return False




#main game loop
while done == False:
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
        vel = 9
        rate = 30
        timer_clr = BLACK

    if pressed[pygame.K_d]:
        cat = pygame.image.load('boned-Pussy.png')
        cat = pygame.transform.scale(cat, (cat_width, cat_height))
        background = bgd
        vel = 7
        rate = 15
        timer_clr = WHITE

    if pressed[pygame.K_s]:
        cat = pygame.image.load('pusspuss.png')
        cat = pygame.transform.scale(cat, (cat_width, cat_height))
        background = bgs
        vel = 5
        rate = 30
        timer_clr = BLACK

    screen.blit(background, (0, 0))
    screen.blit(cat, (xcat,ycat))
    screen.blit(quartercircle1, (0,0))
    screen.blit(quartercircle2, (display_width-quartercircle_width, 0))
    screen.blit(quartercircle3, (0,display_height-quartercircle_height))
    screen.blit(font.render(text, True, (timer_clr)), (0.85*display_width, 0.1*display_height))
    screen.blit(quartercircle4, (display_width-quartercircle_width, display_height-quartercircle_height))

    screen.blit(alpha, (rad1_x, rad1_y))
    screen.blit(alpha, (rad2_x, rad2_y))
    screen.blit(alpha, (rad3_x, rad3_y))
    screen.blit(alpha, (rad4_x, rad4_y))

    rad1_y += rad_speed1*math.cos(rad_traj1)
    rad1_x += rad_speed1*math.sin(rad_traj1)
    rad2_y += rad_speed2*math.cos(rad_traj2)
    rad2_x += rad_speed2*math.sin(rad_traj2)
    rad3_y += rad_speed3*math.cos(rad_traj3)
    rad3_x += rad_speed3*math.sin(rad_traj3)
    rad4_y += rad_speed4*math.cos(rad_traj4)
    rad4_x += rad_speed4*math.sin(rad_traj4)

    #speed factor increasing speed
    if (rad1_x < 0 or rad1_x > display_width or rad1_y < 0 or rad1_y > display_height):
        rad_speed1 += speed_factor
        rad1_x = 1
        rad1_y = 1
        rad_traj1 = random_angle(0, 90)
    if (rad2_x < 0 or rad2_x > display_width or rad2_y < 0 or rad2_y > display_height):
        rad_speed2 += speed_factor
        rad2_x = display_width - 1
        rad2_y = 1
        rad_traj2 = random_angle(270, 360)
    if (rad3_x < 0 or rad3_x > display_width or rad3_y < 0 or rad3_y > display_height):
        rad_speed3 += speed_factor
        rad3_x = 1
        rad3_y = display_height - 1
        rad_traj3 = random_angle(90, 180)
    if (rad4_x < 0 or rad4_x > display_width or rad4_y < 0 or rad4_y > display_height):
        rad_speed4 += speed_factor
        rad4_x = display_width-1
        rad4_y = display_height-1
        rad_traj4 = random_angle(180, 270)

    print("xcat= " + str(xcat))
    print("ycat= " + str(ycat))
    print("rad1_x= " + str(rad1_x))
    print("rad1y= " + str(rad1_y))
    print("rad2x= " + str(rad2_x))
    print("rad2y= " + str(rad2_y))
    print("rad3x= " + str(rad3_x))
    print("rad3y= " + str(rad3_y))
    print("rad4x= " + str(rad4_x))
    print("rad4y= " + str(rad4_y))

    pygame.display.update()

    #check collision

    done = check_collision(rad1_x, rad1_y, xcat, ycat, counter)
    if done == True:
        break
    done = check_collision(rad2_x, rad2_y, xcat, ycat, counter)
    if done == True:
        break
    done = check_collision(rad3_x, rad3_y, xcat, ycat, counter)
    if done == True:
        break
    done = check_collision(rad4_x, rad4_y, xcat, ycat, counter)
    if done == True:
        break
    pygame.time.wait(10)

    pygame.display.flip()
    clock.tick(rate)

screen.blit(background, (0, 0))
largeFont = pygame.font.SysFont(None, 40) # creates a font object
score = largeFont.render('Time alive: '+ str(counter)+ " seconds, well done!",1, BLACK)
screen.blit(score, (200, display_height/2))
pygame.display.update()
pygame.time.wait(5000)
pygame.display.flip()

    

