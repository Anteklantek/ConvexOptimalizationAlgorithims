from utils import get_distances_for_cities

def load_data():
    x1 = 407.6006006264774
    x2 = 211.60881945067894
    x3 = 225.3861460684055
    x4 = 685.6422055756931
    x5 = 574.1923136812239
    x6 = 695.1309349283785
    x7 = 290.76812274071517
    x8 = 318.5215374094178
    x9 = 643.8612451297672
    x10 = 500.8963775188472
    y1 = 490.777645028574
    y2 = 238.69068963870404
    y3 = 498.6441308513401
    y4 = 474.98400413108897
    y5 = 553.5814454116893
    y6 = 453.94846019229277
    y7 = 376.1987891286144
    y8 = 2.960124876782139
    y9 = 564.0891536498484
    y10 = 270.98330387841384


    # x1 = random.random() * 733
    # x2 = random.random() * 733
    # x3 = random.random() * 733
    # x4 = random.random() * 733
    # x5 = random.random() * 733
    # x6 = random.random() * 733
    # x7 = random.random() * 733
    # x8 = random.random() * 733
    # x9 = random.random() * 733
    # x10 = random.random() * 733
    # y1 = random.random() * 733
    # y2 = random.random() * 733
    # y3 = random.random() * 733
    # y4 = random.random() * 733
    # y5 = random.random() * 733
    # y6 = random.random() * 733
    # y7 = random.random() * 733
    # y8 = random.random() * 733
    # y9 = random.random() * 733
    # y10 = random.random() * 733

    distances = get_distances_for_cities()
    starting_tuple_points = [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6), (x7, y7), (x8, y8), (x9, y9), (x10, y10)]
    tuple_points = [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6), (x7, y7), (x8, y8), (x9, y9), (x10, y10)]
    labels = ['Warszawa', 'Kraków', 'Łódź', 'Wrocław', 'Poznań', 'Gdańsk', 'Szczecin', 'Bydgoszcz', 'Lublin', 'Katowice']

    return distances, starting_tuple_points, tuple_points, labels
