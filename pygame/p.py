import pygame
import sys, os

pygame.init()

# create a game window
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('hola')
x, y = screen.get_size()
print(x, y)

#create an image surface
# image = pygame.image.load('alien_invasion/intro_ball.gif')
bg_color = (61, 36, 108)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            sys.exit()
    screen.fill(bg_color)
    # placing that image on the game window
    # screen.blit(image, (600, 400))
    # pygame.draw.circle(screen, (255, 219, 195), (600, 400),100)
    # pygame.draw.rect(screen, (255, 219, 195),(30, 30, 60, 60) )
    pygame.display.flip()