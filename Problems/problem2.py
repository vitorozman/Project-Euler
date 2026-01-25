# https://projecteuler.net/problem=2



def is_even(n):
    return n % 2 == 0


e1 = 1
e2 = 2

fibonacci_seq = [1, 2]
fib_even_sum = 2
while fibonacci_seq[-1] <= 4 * 10**6:
    new_el = fibonacci_seq[-1] + fibonacci_seq[-2]
    if is_even(new_el):
        fib_even_sum += new_el
    fibonacci_seq.append(new_el)

print(fib_even_sum)




