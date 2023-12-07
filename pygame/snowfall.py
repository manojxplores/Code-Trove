import pygame
import sys
import numpy as np

pygame.init()

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
snow_speed = 3

pygame.display.set_caption('Snowfall')

bg_color = (35, 45, 63)

num_snowflakes = 50
snow_fall = np.random.randint(0, 800, (num_snowflakes, 2))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(bg_color)
    for i, x in enumerate(snow_fall):
        pygame.draw.circle(screen, (221, 242, 253), (x[0], int(x[1])), 5)
        snow_fall[i, 1] += snow_speed  # Update the y-coordinate of each snowflake

    for x, y in enumerate(snow_fall):
        pygame.draw.circle(screen, (221, 242, 253), (y[0], y[1]), 3)
        y[1] += snow_speed
    
        if y[1] > screen_height:
            snow_fall[x] = [np.random.randint(0, screen_width), 0]
    
    pygame.display.flip()
    pygame.time.Clock().tick(20)  # Adjust the frame rate
