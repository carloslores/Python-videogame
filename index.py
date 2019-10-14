import pygame 

pygame.init()
screen = pygame.display.set_mode((1200,700))

finished = False
x = 0
y = 50

player_image = pygame.image.load("player.png")
player_image = pygame.transform.scale(player_image, (90,80))
player_image = player_image.convert_alpha()
background_imge = pygame.image.load("ground.jpg")
background_imge = pygame.transform.scale(background_imge, (1200,700))
screen.blit(background_imge, (0,0))

frame = pygame.time.Clock()
while finished == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_SPACE] == 1:
        y += 5
    #rectOne = pygame.Rect(x,y,40,40)#X,Y,WIDTH,HEIGHT
    
    color = (0,0,255)
    white = (255,255,255)
    screen.blit(background_imge,(0, 0))
    screen.blit(player_image, (x,y))
    #pygame.draw.rect(screen,color,rectOne)
    pygame.display.flip()
    frame.tick(30)