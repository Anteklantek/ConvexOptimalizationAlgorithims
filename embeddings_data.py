import random

from calculate_distances import get_distances_for_emmbeddings


def load_data():
    multiplier = 10

    x1 = random.random() * multiplier
    x2 = random.random() * multiplier
    x3 = random.random() * multiplier
    x4 = random.random() * multiplier
    x5 = random.random() * multiplier
    x6 = random.random() * multiplier
    x7 = random.random() * multiplier
    x8 = random.random() * multiplier
    x9 = random.random() * multiplier
    x10 = random.random() * multiplier
    x11 = random.random() * multiplier
    x12 = random.random() * multiplier
    x13 = random.random() * multiplier
    x14 = random.random() * multiplier
    x15 = random.random() * multiplier
    x16 = random.random() * multiplier
    x17 = random.random() * multiplier
    x18 = random.random() * multiplier
    x19 = random.random() * multiplier
    x20 = random.random() * multiplier
    x21 = random.random() * multiplier
    x22 = random.random() * multiplier
    x23 = random.random() * multiplier
    x24 = random.random() * multiplier
    x25 = random.random() * multiplier
    x26 = random.random() * multiplier
    x27 = random.random() * multiplier
    x28 = random.random() * multiplier
    x29 = random.random() * multiplier
    x30 = random.random() * multiplier
    x31 = random.random() * multiplier
    x32 = random.random() * multiplier

    y1 = random.random() * multiplier
    y2 = random.random() * multiplier
    y3 = random.random() * multiplier
    y4 = random.random() * multiplier
    y5 = random.random() * multiplier
    y6 = random.random() * multiplier
    y7 = random.random() * multiplier
    y8 = random.random() * multiplier
    y9 = random.random() * multiplier
    y10 = random.random() * multiplier
    y11 = random.random() * multiplier
    y12 = random.random() * multiplier
    y13 = random.random() * multiplier
    y14 = random.random() * multiplier
    y15 = random.random() * multiplier
    y16 = random.random() * multiplier
    y17 = random.random() * multiplier
    y18 = random.random() * multiplier
    y19 = random.random() * multiplier
    y20 = random.random() * multiplier
    y21 = random.random() * multiplier
    y22 = random.random() * multiplier
    y23 = random.random() * multiplier
    y24 = random.random() * multiplier
    y25 = random.random() * multiplier
    y26 = random.random() * multiplier
    y27 = random.random() * multiplier
    y28 = random.random() * multiplier
    y29 = random.random() * multiplier
    y30 = random.random() * multiplier
    y31 = random.random() * multiplier
    y32 = random.random() * multiplier

    distances = get_distances_for_emmbeddings()
    starting_tuple_points = [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6), (x7, y7), (x8, y8), (x9, y9),
                             (x10, y10), (x11, y11), (x12, y12), (x13, y13), (x14, y14), (x15, y15), (x16, y16),
                             (x17, y17), (x18, y18), (x19, y19), (x20, y20), (x21, y21), (x22, y22), (x23, y23),
                             (x24, y24), (x25, y25), (x26, y26), (x27, y27), (x28, y28), (x29, y29), (x30, y30),
                             (x31, y31), (x32, y32)]
    tuple_points = [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6), (x7, y7), (x8, y8), (x9, y9),
                    (x10, y10), (x11, y11), (x12, y12), (x13, y13), (x14, y14), (x15, y15), (x16, y16), (x17, y17),
                    (x18, y18), (x19, y19), (x20, y20), (x21, y21), (x22, y22), (x23, y23), (x24, y24), (x25, y25),
                    (x26, y26), (x27, y27), (x28, y28), (x29, y29), (x30, y30), (x31, y31), (x32, y32)]
    labels = [
        'warszawa',
        'polska',
        'piłkarz',
        'niemcy',
        'francja',
        'berlin',
        'moskwa',
        'włochy',
        'paryż',
        'rosja',
        'mercedes',
        'hiszpania',
        'praga',
        'rzym',
        'barcelona',
        'bmw',
        'czechy',
        'ateny',
        'fiat',
        'pies',
        'kot',
        'grecja',
        'opel',
        'baran',
        'królik',
        'astra',
        'kucharz',
        'owca',
        'krowa',
        'stolarz',
        'papuga',
        'murarz',
    ]

    return distances, starting_tuple_points, tuple_points, labels
