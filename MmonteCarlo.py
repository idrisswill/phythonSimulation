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
array_of_points = np.zeros((100, 2), dtype=int)
font = pygame.font.Font('freesansbold.ttf', 32)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)












def game(window, width, height, array_length, epocs, origine_coordinate, size_of_square):
    array_of_point = np.zeros((array_length, 2), dtype=int)
    pi_estimation = np.array([])
    clock = pygame.time.Clock()
    fps = 60

    def in_array_or_circle(p):
        '''

        :param p: it is the coordinate for random point
        :return: 0 if point is in circle and 1 if else
        '''
        distance = calculate_distance(p, origine_coordinate)
        return 0 if distance < size_of_square else 1
    for i in range(epocs + 1):
        array_of_point = np.random.randint((origine_coordinate[0], origine_coordinate[1] - size_of_square),
                                           (origine_coordinate[0] + size_of_square, origine_coordinate[1]),
                                           size=(array_length, 2))
        array_of_color = np.array(list(map(in_array_or_circle, array_of_point)))
        unique, counts = np.unique(array_of_color, return_counts=True)
        value_count = dict(zip(unique, counts))
        window.fill((60, 60, 60))
        draw_repere((25, height - 25))
        draw_square_and_circle(5)
        pi = 4 * value_count[0]/array_length
        pi_estimation = np.append(pi_estimation, [pi])
        print(pi_estimation)
        text = font.render(f'nbr:{value_count[0]} / {array_length}', True, green, blue)
        text_pi = font.render(f'pi =:{pi}', True, green, blue)
        textRect = text.get_rect()
        pi_textRect = text_pi.get_rect()
        textRect.center = (width-200, 20)
        pi_textRect.center = (width-200, 60)
        for idx, x in enumerate(array_of_point):
            if array_of_color[idx] == 0:
                pygame.draw.line(window, 'green', tuple(x), tuple(x))
            else:
                pygame.draw.line(window, 'orange', tuple(x), tuple(x))
        window.blit(text, textRect)
        window.blit(text_pi, pi_textRect)
        pygame.display.flip()
        clock.tick(fps)
    print(np.mean(pi_estimation))


def run(window, width, height, nbr_point):
    global array_of_points
    isrun = True
    can_draw_points = False
    clock = pygame.time.Clock()
    fps = 60
    nbr = 0

    while isrun:
        # handling input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isrun = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                can_draw_points = True
        # update
        if nbr < 100:
            array_of_points = np.random.randint((origine_position[0], origine_position[1] - 300),
                                                (origine_position[0] + 300, origine_position[1]),
                                                size=(nbr_point, 2))
            nbr += 1
        else:
            # isrun = False
            continue
        # visuals
        window.fill((60, 60, 60))
        draw_repere((25, HEIGHT - 25))
        draw_square_and_circle(3)
        if can_draw_points:
            core.chrono_start()
            draw_points(array_of_points)
            core.chrono_show()
        # updating the windows
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()


def mesure_run_time_draw_point(nbr_point):
    start_time = time.time()
    array_of_point = np.random.randint((origine_position[0], origine_position[1] - 300),
                                       (origine_position[0] + 300, origine_position[1]),
                                       size=(nbr_point, 2))
    draw_points(array_of_points)
    return time.time() - start_time


if __name__ == "__main__":
    # run(window, WIDTH, HEIGHT, 100000)
    core.chrono_start()
    game(window,WIDTH, HEIGHT, 10000,200,origine_position,500)
    core.chrono_show()
    # iter_number = 1
    # number_of_points = range(1000, 1000000, 1000)
    # run_times = [mesure_run_time_draw_point(nbr)*iter_number for nbr in number_of_points]
    # model = np.polyfit(number_of_points, run_times, 1)
    # print(model)
    # plt.scatter(number_of_points, run_times)
    # plt.xlabel('Number of point')
    # plt.ylabel('Runtime')
    # plt.show()
