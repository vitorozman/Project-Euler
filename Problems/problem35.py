# https://projecteuler.net/problem=35


from useful_functions.prime_numbers import is_prime


def digits_rotations(n):
    digits = [k for k in str(n)]
    if len(digits) == 1:
        return str(n)
    nums = set()
    for i, d in enumerate([k for k in str(n)]):
        digits.pop(i)
        nums.add(d + digits_rotations(int(''.join(digits))))
    return nums
