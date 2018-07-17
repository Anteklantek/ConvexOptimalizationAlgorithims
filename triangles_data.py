import numpy as np



def load_data():
    x1 = 3  # random.random() * 5
    x2 = 3  # random.random() * 5
    x3 = 7  # random.random() * 5
    y1 = 3  # random.random() * 5
    y2 = 11  # random.random() * 5
    y3 = 10  # random.random() * 5

    # x1 = 3
    # x2 = 6
    # x3 = 3
    # y1 = 3
    # y2 = 3
    # y3 = 7

    distances = np.array([[0, 3, 4], [3, 0, 5], [4, 5, 0]])
    tuple_points = [(x1, y1), (x2, y2), (x3, y3)]
    starting_tuple_points = [(x1, y1), (x2, y2), (x3, y3)]
    labels = ["Point 1", "Point 2", "Point 3"]

    return distances, starting_tuple_points, tuple_points, labels