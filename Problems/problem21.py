# https://projecteuler.net/problem=21

from useful_functions.prime_numbers import find_divisors


divisor_sums = {}
amicable_nums = set()
for n in range(1, 10001):
    # print(divisor_sums)
    if n in amicable_nums:
        continue
    if n in divisor_sums:
        divisor_sum = divisor_sums[n]
    else:
        divisor_sum = sum(find_divisors(n)) - n
        divisor_sums[n] = divisor_sum

    if divisor_sum == n:
        continue

    if divisor_sum not in divisor_sums:
        divisor_sum2 = sum(find_divisors(divisor_sum)) - divisor_sum
        divisor_sums[divisor_sum] = divisor_sum2
        if divisor_sum2 == n:
            amicable_nums.add(divisor_sum2)
            amicable_nums.add(n)
    else:
        if divisor_sums[divisor_sum] == n:
            amicable_nums.add(divisor_sum)
            amicable_nums.add(n)

print(amicable_nums)
for i in amicable_nums:
    print(i, divisor_sums[i])
print(sum(amicable_nums))

