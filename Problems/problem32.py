# https://projecteuler.net/problem=32

def is_pandigital(m1, m2, p):
    digits = str(m1) + str(m2) + str(p)
    if len(digits)<9:
        return False
    list_dig = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in list_dig:
        digits = digits.replace(i, '', 1)
    return len(digits)==0

def all_pandigital():
    pandigital = set()
    for n in range(1, 100):
        for m in range(10000):
            p = n*m
            if is_pandigital(n, m, p):
                pandigital.add(p)
    return list(pandigital)

print(sum(all_pandigital()))