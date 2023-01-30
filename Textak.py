import sys
import pygame
pygame.init()
#--------------------- ROZLISENÍ + .PNG
ROZLISENI = ROZLISENI_X, ROZLISENI_Y = 1920, 1017
FPS_COUNT = 60
textura = pygame.image.load("Formula1.png")
#--------------------- POZICE + ROZMĚR
rozmer_y = 50
rozmer_x = 50
pozice_x = 500
pozice_y = 600
rychlost = 1
#--------------------- OKNO
okno = pygame.display.set_mode(ROZLISENI)
pygame.display.set_caption('Formule1')
#--------------------- ZAVÍRÁNÍ
while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    klavesnice = pygame.key.get_pressed()
    if klavesnice[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
#------------------------------ OKNO + TEXTURA
    okno.fill((250, 250, 250))
    okno.blit(textura,(pozice_x, pozice_y))
    pygame.display.update()
#------------------------------ POHYB
    accleration_key = klavesnice[pygame.K_LEFT] or klavesnice[pygame.K_RIGHT] or klavesnice[pygame.K_UP] or klavesnice[pygame.K_DOWN]
    accleration_key_Nitro_Left_Right = klavesnice[pygame.K_UP] or klavesnice[pygame.K_DOWN]
    accleration_key_Nitro_Up_Down = klavesnice[pygame.K_RIGHT] or klavesnice[pygame.K_LEFT]
    
    klavesnice = pygame.key.get_pressed()
    if klavesnice[pygame.K_LEFT]:
        pozice_x -= rychlost
    if klavesnice[pygame.K_RIGHT]:
        pozice_x += rychlost
    if klavesnice[pygame.K_UP]:
        pozice_y -= rychlost
    if klavesnice[pygame.K_DOWN]:
        pozice_y += rychlost
#------------------------------ NITRO LEFT RIGHT
    if klavesnice[pygame.K_LSHIFT] and accleration_key:
        if rychlost <= 3:
            rychlost = rychlost + 0.1 
    else:
            if rychlost >= 1:
                rychlost = rychlost - 0.1
    
    if klavesnice[pygame.K_LSHIFT] and accleration_key and accleration_key_Nitro_Left_Right:
        if rychlost > 1:
            rychlost = rychlost - 0.1
    else:
            if rychlost <= 1:
                rychlost = rychlost + 0.1
    
    if klavesnice[pygame.K_LSHIFT] and accleration_key_Nitro_Left_Right and accleration_key:
        if rychlost > 1:
            rychlost = rychlost - 0.1
    else:
            if rychlost <= 1:
                rychlost = rychlost + 0.1
#------------------------------ NITRO UP DOWN

#------------------------------ BORDER
    if pozice_x < 0:
        pozice_x = 0
    if pozice_y < 0:
        pozice_y = 0
    if pozice_x > ROZLISENI_X - rozmer_x:
        pozice_x = ROZLISENI_X - rozmer_x
    if pozice_y > ROZLISENI_Y - rozmer_y:
        pozice_y = ROZLISENI_Y - rozmer_y
#------------------------------ ROTACE
    
    
    
    
    
    
    
    
    