import pygame 

pygame.init()
screen = pygame.display.set_mode((900, 700))

finished = False
x = 0
y = 50
frame = pygame.time.Clock()
while finished == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_SPACE] == 1:
        y += 5
    rectOne = pygame.Rect(x,y,30,30)#X,Y,WIDTH,HEIGHT
    
    color = (0,0,255)
    black = (0,0,0)
    screen.fill(black)
    pygame.draw.rect(screen,color,rectOne)
    pygame.display.flip()
    frame.tick(30)