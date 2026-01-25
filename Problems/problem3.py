# https://projecteuler.net/problem=3


def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):  # Check divisibility up to the square root of num
        if num % i == 0:
            return False
    return True

def factorize(n):
    if is_prime(n):
        return n
    else:
        for i in range(2, int(n**0.5)+1):
            if (n % i == 0) and (is_prime(i)):
                print(i)
                childe = factorize(n//i)
                if type(childe)==list:
                    return [i] + childe
                else:
                    return [i, childe]


factorization = factorize(600851475143)
print(factorization[-1])
