# https://projecteuler.net/problem=9


def check_pythagorean(a, b, c):
    return a**2 + b**2 == c**2

limit = 1000
for a in range(1, limit):
    b_limit = 500 - a//2 + 1
    for b in range(a, b_limit):
        c = 1000 - a - b
        if check_pythagorean(a, b, c):
            print(f"{a}x{b}x{c} =", a*b*c)

