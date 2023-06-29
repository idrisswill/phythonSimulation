import time
from functions import non_graphical_function, graphic_function
import matplotlib.pyplot as plt
import pygame
import math
import numpy as np
import sys
from helper import core

# initialize pygame

pygame.init()
# define the windows

WIDTH, HEIGHT = 1280, 960
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('monte Carlo Simulation')

ORIGIN_COORDINATE = (25, HEIGHT - 25)
GRADUATION_INTERVAL = 100
run = True
fps = 60
clock = pygame.time.Clock()
size_of_square = 6 * GRADUATION_INTERVAL
array_of_point = np.random.randint((ORIGIN_COORDINATE[0], ORIGIN_COORDINATE[1] - size_of_square),
                                           (ORIGIN_COORDINATE[0] + size_of_square, ORIGIN_COORDINATE[1]),
                                           size=(1000, 2))

if __name__ == "__main__":
    while run:
        # handling input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            # update
            # visuals
        window.fill((20, 20, 20))
        graphic_function.draw_coordinate_system(ORIGIN_COORDINATE,GRADUATION_INTERVAL, window)
        graphic_function.draw_square_and_circle(6*GRADUATION_INTERVAL, ORIGIN_COORDINATE, window)
        graphic_function.draw_points(array_of_point, window)
        # updating the windows
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
