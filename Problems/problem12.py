# https://projecteuler.net/problem=12



def find_divisors(n):
    divisors = []
    
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:

            if n // i == i:
                divisors.append(i)
            else:
                
                # Add both divisors
                divisors.append(i)
                divisors.append(n // i)
    return divisors


def find_triangle_numbers_with_k_divisors(k):
    triangle_numbers = [1]
    s = 2
    while True:
        n = triangle_numbers[-1] + s
        if len(find_divisors(n)) > k:
            return n
        # print(triangle_numbers, n)
        triangle_numbers.append(n)
        s += 1

print(find_triangle_numbers_with_k_divisors(500))


