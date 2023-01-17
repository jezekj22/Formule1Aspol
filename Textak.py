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
rychlost2 = 3
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
    klavesnice = pygame.key.get_pressed()
    if klavesnice[pygame.K_LEFT]:
        pozice_x -= rychlost
    if klavesnice[pygame.K_RIGHT]:
        pozice_x += rychlost
    if klavesnice[pygame.K_UP]:
        pozice_y -= rychlost
    if klavesnice[pygame.K_DOWN]:
        pozice_y += rychlost
#------------------------------ NITRO    
    if klavesnice[pygame.K_LSHIFT] and klavesnice[pygame.K_LEFT]:
        if rychlost <= 3:
            rychlost = rychlost + 0.01
    else:
        if klavesnice[pygame.K_LSHIFT] and klavesnice[pygame.K_LEFT] and klavesnice[pygame.K_UP]:
            if rychlost >= 1:
                rychlost = rychlost - 0.01
    
#------------------------------ BORDER
    if pozice_x < 0:
        pozice_x = 0
    if pozice_y < 0:
        pozice_y = 0
    if pozice_x > ROZLISENI_X - rozmer_x:
        pozice_x = ROZLISENI_X - rozmer_x
    if pozice_y > ROZLISENI_Y - rozmer_y:
        pozice_y = ROZLISENI_Y - rozmer_y
    
    
    
    
    
    
    
    
    