import math as m

import matplotlib.pyplot as plt
from utils import function_cost, gradient_element, argmin_dych, distance, numerical_gradient_element
from cities_data import load_data as c_load_data
from triangles_data import load_data as t_load_data
from line_data import load_data as l_load_data

ALPHA_STARTING_POINTS_VALUE = 0.1

alpha_cauchy = False
number_of_dych_iterations = 100

alpha_sqrt = False

alpha_const_step = True
alpha_step_size = 0.0005

number_of_iterations = 500

distances, tuple_points, starting_tuple_points, labels = l_load_data()

gradient = []

for i in range(len(tuple_points)):
    x_gradient = gradient_element(tuple_points, i, 0, distances)
    y_gradient = gradient_element(tuple_points, i, 1, distances)
    gradient.append((x_gradient, y_gradient))

numerical_gradient = []
for i in range(len(tuple_points)):
    x_gradient = numerical_gradient_element(tuple_points, i, 0, distances)
    y_gradient = numerical_gradient_element(tuple_points, i, 1, distances)
    numerical_gradient.append((x_gradient, y_gradient))

print("gradient: ", gradient)
print("numerical ", numerical_gradient)

print("cost: ", function_cost(tuple_points, distances))

error_in_time = []

for k in range(1, number_of_iterations):
    print("iteration: ", k)

    if alpha_sqrt:
        alpha = 1 / m.sqrt(k)
    if alpha_const_step:
        alpha = alpha_step_size
    if alpha_cauchy:
        argmin_error_in_time = []
        alpha = argmin_dych(tuple_points, gradient, number_of_dych_iterations)
        plt.plot(list(range(1, len(argmin_error_in_time) + 1)), argmin_error_in_time)
        plt.show()
    print("alpha: ", alpha)

    for i in range(len(tuple_points)):
        new_x = tuple_points[i][0] - alpha * gradient[i][0]
        new_y = tuple_points[i][1] - alpha * gradient[i][1]
        tuple_points[i] = (new_x, new_y)

    function_value = function_cost(tuple_points, distances)

    error_in_time.append(function_value)

    print("new function cost")
    print(function_value)

    gradient = []
    for i in range(len(tuple_points)):
        x_gradient = gradient_element(tuple_points,i,0,distances)
        y_gradient = gradient_element(tuple_points,i,1, distances)
        gradient.append((x_gradient, y_gradient))


print("end function costs and points")
print("function_cost: ", function_cost(tuple_points, distances))
print("tuple_points: ", tuple_points)
print("starting_tuple_points: ", starting_tuple_points)
print(distance(tuple_points[0], tuple_points[1]))
print(distance(tuple_points[0], tuple_points[2]))
print(distance(tuple_points[1], tuple_points[2]))

# plt.subplot(211)
# middle = int(len(linear_points) / 2)
# for i in range(middle):
#     plt.plot(linear_points[i], linear_points[i + middle], 'ro')
#     plt.plot(starting_linear_points[i], starting_linear_points[i + middle], 'bo', alpha=ALPHA_STARTING_POINTS_VALUE)
#     plt.text(linear_points[i] * 1.01, linear_points[i + middle] * 1.001, labels[i], fontsize=8)
#     plt.text(starting_linear_points[i] * 1.01, starting_linear_points[i + middle] * 1.001, labels[i], fontsize=8,
#              alpha=ALPHA_STARTING_POINTS_VALUE)
# plt.ylabel('y')
# plt.xlabel('x')
# plt.gca().set_aspect('equal', adjustable='box')
#
# plt.subplot(212)
# if alpha_const_step:
#     plt.title("step size: " + str(alpha_step_size))
# plt.plot(list(range(1, len(error_in_time) + 1)), error_in_time)
#
# plt.show()
