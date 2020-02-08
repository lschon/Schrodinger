import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Schrodinger's Cat")

#set colours
black = (0,0,0)
white = (255,255,255)
pink = (249,184,210)

clock = pygame.time.Clock()
pussyPic = pygame.image.load('the_main_pussy.png')
done = False
# cat sprite
def pussy(x,y):
    gameDisplay.blit(pussyPic, (x,y))

x = (display_width * 0)
y = (display_height * 0)
#main game loop

print("Checkpoint1")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    print("Checkpoint2")


    gameDisplay.fill(pink)
    pussy(x,y)

    pygame.display.update()
    print("checkpoint3")
    clock.tick(60)



pygame.quit()
quit()
