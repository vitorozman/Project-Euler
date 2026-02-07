# https://projecteuler.net/problem=23

from useful_functions.prime_numbers import find_divisors

def find_all_abundant(limit):
    abundant = []
    for n in range(1, limit):
        div_sum = sum(find_divisors(n))-n
        if div_sum > n:
            abundant.append(n)
    return abundant


limit = 28123
total_sum = sum([i for i in range(limit)])

abundant_nums = find_all_abundant(limit)
abundant_sum = set()
for num1 in abundant_nums:
    for num2 in abundant_nums:
        num = num1 + num2
        if num < limit:
            abundant_sum.add(num)

print(total_sum-sum(abundant_sum))