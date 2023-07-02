import math
import globals


def calculate_distance(p1, p2):
    return math.sqrt((p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2)


def is_it_in_the_circle(p):
    '''
    :param p: it is the coordinate for random point
    :return: 0 if point is in circle and 1 if else
    '''

    distance = calculate_distance(p, globals.ORIGIN_COORDINATE)
    return 0 if distance < globals.SIZE_OF_SQUARE * globals.GRADUATION_INTERVAL else 1
