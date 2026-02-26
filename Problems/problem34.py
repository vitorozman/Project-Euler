# https://projecteuler.net/problem=34

from math import factorial

def find_curious_numbers():
    curious_numbers = []
    for n in range(10, factorial(10)):
        sum_num = 0
        for i in str(n):
            sum_num += factorial(int(i))
        if n == sum_num:
            curious_numbers.append(n)
    return sum(curious_numbers)

print(find_curious_numbers())
