# https://projecteuler.net/problem=10

from useful_functions.prime_numbers import is_prime



def sum_primes_bellow(N):
    n = 2
    current_sum = 0
    while n < N:
        if is_prime(n):
            current_sum += n
        n += 1
    return current_sum

# print(sum_primes_bellow(10))
print(sum_primes_bellow(2*10**6))