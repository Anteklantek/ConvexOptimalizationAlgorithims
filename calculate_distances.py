import csv
import math as m
import numpy as np

#elements as list of strings with first item being word itself
def calculate_distance_between_two_elements(element1, element2):
    sum = 0

    for i in range(1, len(element1)):
        print("elem1: ", element1[i], "elem2: ", element2[i])
        sum += (float(element1[i]) - float(element2[i]))**2

    return m.sqrt(sum)



def get_distances_for_emmbeddings():
    distances_from_file = np.loadtxt("emmbedding_data.txt", delimiter=" ")
    return distances_from_file


list_of_words = []

with open('embeddings.txt', 'r') as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        list_of_words.append(row)


distances = np.zeros(shape=(len(list_of_words), len(list_of_words)))

for i in range(len(list_of_words)):
    for j in range(i+1, len(list_of_words)):
        distance = calculate_distance_between_two_elements(list_of_words[i], list_of_words[j])
        distances[i, j] = distance
        distances[j, i] = distance

np.savetxt("emmbedding_data.txt",distances,delimiter=" ")

