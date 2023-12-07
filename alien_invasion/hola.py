import pygame
import os, sys

pygame.init() #initializing all the pygame modules

screen = pygame.display.set_mode((1200, 800), pygame.RESIZABLE) #create a game window
pygame.display.set_caption('Hola')

x, y = screen.get_size()

bg_color = (255, 219, 195)

print(x, y)
while True:
    # if bg_color == 'red':
    #     bg_color = 'green'
    # else:
    #     bg_color = 'red'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        screen.fill(bg_color)
        pygame.draw.circle(screen, (0, 0, 0), (300, 200), 75)
        pygame.display.flip()


