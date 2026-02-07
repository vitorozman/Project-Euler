# https://projecteuler.net/problem=22

import string

def load_txt_file(filename):
    with open(filename) as f:
        names = f.readlines()
    names = names[0].replace('"', '').split(",")
    names.sort()
    return names

def create_letters_score():
    alphabet = list(string.ascii_uppercase)
    letters_score = {}
    for i, k in enumerate(alphabet):
        letters_score[k] = i+1
    return letters_score


def evaluate_names_sum(names, letters_score):
    total_sum = 0
    for i, name in enumerate(names):
        name_score = 0
        for l in name:
            name_score += letters_score[l]
        total_sum += (i+1)*name_score
    return total_sum


names = load_txt_file('Problems/names.txt')
print(evaluate_names_sum(names, create_letters_score()))