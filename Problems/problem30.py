# https://projecteuler.net/problem=30


def digit_power_sum(num, p):
    return sum([int(k)**p for k in str(num)])

power_sum = []
for n in range(10, 10**6):
    if digit_power_sum(n, 5) == n:
        power_sum.append(n)
print(sum(power_sum))
