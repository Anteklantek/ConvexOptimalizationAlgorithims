import csv

import numpy as np

#elements as list of strings with first item being word itself
def calculate_distance_between_two_elements(element1, element2):
    sum = 0
    number_of_components = 0

    for i in range(1, len(element1)):
        print("elem1: ", element1[i], "elem2: ", print(element2[i]))
        sum += (float(element1[i]) - float(element2[i]))**2
        number_of_components += 1


list_of_words = []

with open('embeddings.txt', 'r') as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        list_of_words.append(row)


distances = np.zeros(shape=(len(list_of_words), len(list_of_words)))

print(list_of_words[0])

calculate_distance_between_two_elements(list_of_words[0], list_of_words[1])


