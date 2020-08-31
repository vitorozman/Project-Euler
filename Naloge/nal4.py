from itertools import combinations


def najvecji_palindrom():
    sez = []
    for a, b in combinations(range(900, 1000), 2):
        if str(a * b) == str(a * b)[::-1]:
            sez.append(a * b)
    return max(sez)

print(najvecji_palindrom())
906609