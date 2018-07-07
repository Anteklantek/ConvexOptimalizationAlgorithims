import numpy as np


def load_data():
    x1 = 1  # random.random() * 4
    x2 = 3  # random.random() * 4
    x3 = 3  # random.random() * 4
    x4 = 6  # random.random() * 4
    x5 = 5  # random.random() * 4
    y1 = 8  # random.random() * 4
    y2 = 2  # random.random() * 4
    y3 = 4  # random.random() * 4
    y4 = 6  # random.random() * 4
    y5 = 10  # random.random() * 4

    distances = np.array([[0, 1, 2, 3, 4], [1, 0, 1, 2, 3], [2, 1, 0, 1, 2], [3, 2, 1, 0, 1], [4, 3, 2, 1, 0]])
    tuple_points = [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)]
    starting_tuple_points = [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)]
    labels = ["Point 1", "Point 2", "Point 3", "Point 4", "Point 5"]

    return distances, starting_tuple_points, tuple_points, labels
