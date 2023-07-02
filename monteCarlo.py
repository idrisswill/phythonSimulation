import time
from functions import non_graphical_function, graphic_function
import globals
import matplotlib.pyplot as plt
import pygame
import math
import numpy as np
import sys
from helper import core

# initialize pygame

pygame.init()
globals.initialize()
# define the windows


window = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT))
pygame.display.set_caption('monte Carlo Simulation')

run = True
fps = 60
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 32)
# define color of text
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

size_of_square = 6 * globals.GRADUATION_INTERVAL
array_of_point = np.random.randint((globals.ORIGIN_COORDINATE[0], globals.ORIGIN_COORDINATE[1] - size_of_square),
                                           (globals.ORIGIN_COORDINATE[0] + size_of_square, globals.ORIGIN_COORDINATE[1]),
                                           size=(globals.N_TOTAL, 2))

is_in_circle = np.array(list(map(non_graphical_function.is_it_in_the_circle, array_of_point)))
unique, counts = np.unique(is_in_circle, return_counts=True)
value_count = dict(zip(unique, counts))
pi_estimate = 4 * value_count[0] / globals.N_TOTAL
if __name__ == "__main__":
    epoc = 1
    array_of_pi_estimation = np.array([])
    while run:
        # handling input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        # update
        epoc+=1
        if epoc < globals.EPOCS:
            array_of_point = np.random.randint(
                (globals.ORIGIN_COORDINATE[0], globals.ORIGIN_COORDINATE[1] - size_of_square),
                (globals.ORIGIN_COORDINATE[0] + size_of_square, globals.ORIGIN_COORDINATE[1]),
                size=(globals.N_TOTAL, 2))

            is_in_circle = np.array(list(map(non_graphical_function.is_it_in_the_circle, array_of_point)))
            unique, counts = np.unique(is_in_circle, return_counts=True)
            value_count = dict(zip(unique, counts))
            pi_estimate = 4 * value_count[0] / globals.N_TOTAL
            array_of_pi_estimation = np.append(array_of_pi_estimation, [pi_estimate])
        else:
            pi = np.mean(array_of_pi_estimation)
            text_final_pi = font.render(f'The final value of the Pi estimate is equal to {pi} almost surely', True, green, blue)
            text_final_piRect = text_final_pi.get_rect()
            text_final_piRect.center = (globals.WIDTH/2, globals.HEIGHT/2)


            # visuals
        window.fill((20, 20, 20))
        graphic_function.draw_coordinate_system(globals.ORIGIN_COORDINATE, globals.GRADUATION_INTERVAL, window)
        graphic_function.draw_square_and_circle(6*globals.GRADUATION_INTERVAL, globals.ORIGIN_COORDINATE, window)
        graphic_function.draw_points(array_of_point, is_in_circle, window)
        text = font.render(f'Points: {value_count[0]} / {globals.N_TOTAL}', True, green, blue)
        text_pi = font.render(f'pi ≃ {pi_estimate}', True, green, blue)
        textRect = text.get_rect()
        pi_textRect = text_pi.get_rect()
        textRect.center = (globals.WIDTH - 200, 20)
        pi_textRect.center = (globals.WIDTH - 200, 60)
        window.blit(text, textRect)
        window.blit(text_pi, pi_textRect)
        if epoc >= globals.EPOCS:
            window.blit(text_final_pi, text_final_piRect)

        # updating the windows
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
