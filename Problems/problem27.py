# https://projecteuler.net/problem=27


from useful_functions.prime_numbers import is_prime

list_primes = [n for n in range(1, 999, 2) if is_prime(n)]
print(list_primes)
a, b, l = 0, 0, 0
for p in list_primes:
    for i in range(-999, 999, 2):
        n = 0
        fn = p
        while is_prime(fn):
            n += 1
            fn = n**2 + n*i + p
        if n > l:
            l = n
            a = i
            b = p
print('a:', a, 'b:', b, 'len fn:', l)
print(a*b)