import pygame


def draw_coordinate_system(origin_coordinate, graduation_interval, window):
    width, height = pygame.display.get_surface().get_size()
    pygame.draw.line(window, "red", (origin_coordinate[0], 0), (origin_coordinate[0], height), 2)
    pygame.draw.line(window, "blue", (0, origin_coordinate[1]), (width, origin_coordinate[1]), 2)
    x = 0
    # draw graduation
    while x < height - origin_coordinate[0]:
        x += graduation_interval
        pygame.draw.line(window, "red", (origin_coordinate[0] + 5, origin_coordinate[1] - x),
                         (origin_coordinate[0] - 5, (origin_coordinate[1] - x)), 1)
        pygame.draw.line(window, "blue", (origin_coordinate[0] + x, origin_coordinate[1] - 5),
                         (origin_coordinate[0] + x, (origin_coordinate[1] + 5)), 1)


def draw_points(array_of_points, window):
    '''
        :param array_of_points: the array of coordinates of the points to draw
        :param window: window where we can draw
        :return: void
        '''
    for point in array_of_points:
        pygame.draw.line(window, 'orange', tuple(point), tuple(point))


def draw_square_and_circle(radius, center, window):
    '''
    :param window: window where we can draw fig
    :param center: the center of circle
    :param radius: t is an integer for multiply graduation interval
    :return: void
    '''

    square = pygame.Rect(center[0], center[1] - radius, radius, radius)
    pygame.draw.rect(window, "green", square, 1)
    pygame.draw.circle(window, 'yellow', center, radius, 1)
