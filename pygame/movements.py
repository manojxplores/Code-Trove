import pygame
import os , sys

pygame.init()

# creating a game window
win = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('test')

x = 50
y = 50
width = 40
height = 60
vel = 5

# Setting up the game loop
while True:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    pygame.draw.rect(win, "RED", (x, y, width, height) )
    pygame.display.update() #updating the screen