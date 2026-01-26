# https://projecteuler.net/problem=6

def sum_square(n):
    return sum([k**2 for k in range(1, n+1)])

def square_sum(n):
    return sum([k for k in range(1, n+1)])**2


print(square_sum(100)- sum_square(100))