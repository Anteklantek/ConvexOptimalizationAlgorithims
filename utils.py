import csv
import math as m

import numpy as np

NUMERICAL_GRADIENT_DELTA = 0.00000000000001
DYCH_LEFT = 0.0000000000000000001
DYCH_RIGHT = 20


def get_distances_for_cities():
    distances = np.zeros(shape=(10, 10))

    with open('cities', 'r') as f:
        reader = csv.reader(f, delimiter=' ')
        i = 0
        for row in reader:
            j = 0
            for number in row:
                distances[i, j] = number
                j += 1
            i += 1
    return distances


def distance(point1, point2):
    dx = point1[0] - point2[0]
    dy = point1[1] - point2[1]
    return ((dx ** 2) + (dy ** 2)) ** 0.5


def function_cost(tuple_points_arg, distances):
    summy = 0
    for i in range(len(tuple_points_arg)):
        for j in range(i + 1, len(tuple_points_arg)):
            summy += (m.sqrt((tuple_points_arg[i][0] - tuple_points_arg[j][0]) ** 2 + (
                    tuple_points_arg[i][1] - tuple_points_arg[j][1]) ** 2) - distances.item(
                i, j)) ** 2
    return summy


# 0 for x, 1 for y
def numerical_gradient_element(tuple_points_arg, elem_index, x_or_y, distances):
    delta = NUMERICAL_GRADIENT_DELTA
    new_tuple_points_left = tuple_points_arg.copy()
    new_tuple_points_right = tuple_points_arg.copy()
    if x_or_y == 0:
        new_tuple_points_left[elem_index] = (
            new_tuple_points_left[elem_index][0] - delta, new_tuple_points_left[elem_index][1])
        new_tuple_points_right[elem_index] = (
            new_tuple_points_right[elem_index][0] + delta, new_tuple_points_right[elem_index][1])
    if x_or_y == 1:
        new_tuple_points_left[elem_index] = (
            new_tuple_points_left[elem_index][0], new_tuple_points_left[elem_index][1] - delta)
        new_tuple_points_right[elem_index] = (
            new_tuple_points_right[elem_index][0], new_tuple_points_right[elem_index][1] + delta)

    function_cost_left = function_cost(new_tuple_points_left, distances)
    function_cost_right = function_cost(new_tuple_points_right, distances)

    sum = function_cost_right + function_cost_left

    return (function_cost_right - function_cost_left) / (2 * delta)


def argmin_dych_function_cost(tuple_points_arg, tuple_gradient_arg, alpha, distances):
    new_arguments = []

    for i in range(len(tuple_points_arg)):
        new_x = tuple_points_arg[i][0] - alpha * tuple_gradient_arg[i][0]
        new_y = tuple_points_arg[i][1] - alpha * tuple_gradient_arg[i][1]
        new_arguments.append((new_x, new_y))

    return function_cost(new_arguments, distances)


# 0 for x, 1 for y
def gradient_element(tuple_points_arg, elem_index, x_or_y, distances):
    summy = 0
    for i in range(len(tuple_points_arg)):
        if i < elem_index:
            upper = 2 * (tuple_points_arg[i][x_or_y] - tuple_points_arg[elem_index][x_or_y]) * (
                    m.sqrt((tuple_points_arg[elem_index][0] - tuple_points_arg[i][0]) ** 2 + (
                            tuple_points_arg[elem_index][1] - tuple_points_arg[i][1]) ** 2) - distances.item(
                (elem_index, i)))

            divide_by = m.sqrt((
                    (tuple_points_arg[elem_index][0] - tuple_points_arg[i][0]) ** 2 +
                    (tuple_points_arg[elem_index][1] - tuple_points_arg[i][1]) ** 2)
            )
            summy -= upper / divide_by
        if i > elem_index:
            upper = 2 * (tuple_points_arg[elem_index][x_or_y] - tuple_points_arg[i][x_or_y]) * (
                    m.sqrt((tuple_points_arg[elem_index][0] - tuple_points_arg[i][0]) ** 2 + (
                            tuple_points_arg[elem_index][1] - tuple_points_arg[i][1]) ** 2) - distances.item(
                (elem_index, i)))

            divide_by = m.sqrt((
                    (tuple_points_arg[elem_index][0] - tuple_points_arg[i][0]) ** 2 +
                    (tuple_points_arg[elem_index][1] - tuple_points_arg[i][1]) ** 2)
            )
            summy += upper / divide_by
    return summy


def argmin_dych(tuple_points_arg, tuple_gradient_arg, number_of_iterations, distances):
    a = DYCH_LEFT
    b = DYCH_RIGHT
    for k in range(number_of_iterations):
        m = (a + b) / 2
        x1 = m - 0.00000001
        x2 = m + 0.00000001
        fx1 = argmin_dych_function_cost(tuple_points_arg, tuple_gradient_arg, x1, distances)
        fx2 = argmin_dych_function_cost(tuple_points_arg, tuple_gradient_arg, x2, distances)
        if fx1 <= fx2:
            b = x2
        else:
            a = x1
    return (a + b) / 2


def calculate_gradient(tuple_points, distances):
    gradient_to_return = []
    for i in range(len(tuple_points)):
        x_gradient = gradient_element(tuple_points, i, 0, distances)
        y_gradient = gradient_element(tuple_points, i, 1, distances)
        gradient_to_return.append((x_gradient, y_gradient))
    return gradient_to_return


def perform_one_step_towards_gradient(tuple_points, gradient, alpha):
    new_tuple_points = []
    for i in range(len(tuple_points)):
        new_x = tuple_points[i][0] - alpha * gradient[i][0]
        new_y = tuple_points[i][1] - alpha * gradient[i][1]
        new_tuple_points.append((new_x, new_y))
    return new_tuple_points
