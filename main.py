import math as m
import matplotlib.pyplot as plt

from utils import function_cost, argmin_dych, distance, numerical_gradient_element, calculate_gradient, \
    perform_one_step_towards_gradient
from triangles_data import load_data as t_load_data

ALPHA_COLOR_STARTING_POINTS_VALUE = 0.1

NUMBER_OF_ITERATIONS = 20

ALPHA_CAUCHY = True
NUMBER_OF_DYCH_ITERATIONS = 10

ALPHA_SQRT = False

ALPHA_CONST_STEP = False
ALPHA_STEP_SIZE = 0.0005

distances, tuple_points, starting_tuple_points, labels = t_load_data()

gradient = calculate_gradient(tuple_points, distances)

numerical_gradient = []
for i in range(len(tuple_points)):
    x_gradient = numerical_gradient_element(tuple_points, i, 0, distances)
    y_gradient = numerical_gradient_element(tuple_points, i, 1, distances)
    numerical_gradient.append((x_gradient, y_gradient))

print("gradient: ", gradient)
print("numerical ", numerical_gradient)

print("cost: ", function_cost(tuple_points, distances))

error_in_time = [function_cost(tuple_points, distances)]

for k in range(1, NUMBER_OF_ITERATIONS):
    print("iteration: ", k)

    alpha = 0
    if ALPHA_SQRT:
        alpha = 1 / m.sqrt(k)
    if ALPHA_CONST_STEP:
        alpha = ALPHA_STEP_SIZE
    if ALPHA_CAUCHY:
        alpha = argmin_dych(tuple_points, gradient, NUMBER_OF_DYCH_ITERATIONS, distances)
    print("alpha: ", alpha)

    tuple_points = perform_one_step_towards_gradient(tuple_points, gradient, alpha)

    function_value = function_cost(tuple_points, distances)
    error_in_time.append(function_value)
    print("new function cost")
    print(function_value)

    gradient = calculate_gradient(tuple_points, distances)

print("end function cost: ", function_cost(tuple_points, distances))
print("tuple points: ", tuple_points)
print("starting tuple points: ", starting_tuple_points)

plt.subplot(211)
xs = [elem[0] for elem in tuple_points]
ys = [elem[1] for elem in tuple_points]
starting_xs = [elem[0] for elem in starting_tuple_points]
starting_ys = [elem[1] for elem in starting_tuple_points]

for i in range(len(xs)):
    plt.plot(xs[i], ys[i], 'ro')
    plt.plot(starting_xs[i], starting_ys[i], 'bo', alpha=ALPHA_COLOR_STARTING_POINTS_VALUE)
    plt.text(xs[i] * 1.01, ys[i] * 1.001, labels[i], fontsize=8)
    plt.text(starting_xs[i] * 1.01, starting_ys[i] * 1.001, labels[i], fontsize=8, alpha=ALPHA_COLOR_STARTING_POINTS_VALUE)
plt.ylabel('y')
plt.xlabel('x')
plt.gca().set_aspect('equal', adjustable='box')

plt.subplot(212)
if ALPHA_CONST_STEP:
    plt.title("step size: " + str(ALPHA_CONST_STEP))
plt.plot(list(range(1, len(error_in_time) + 1)), error_in_time)

plt.show()
