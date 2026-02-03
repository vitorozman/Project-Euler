# https://projecteuler.net/problem=16


def digit_sum(n):
    str_n = str(n)
    current_sum = 0
    for i in str_n:
        current_sum += int(i)
    return current_sum

print(digit_sum(2**1000))


