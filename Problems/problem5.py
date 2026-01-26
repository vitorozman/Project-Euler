# https://projecteuler.net/problem=5

from useful_functions.prime_numbers import factorize

def min_evenly_divisible(to_num):
    state_list = []
    for n in range(1, to_num):
        left = []
        for k in factorize(n):
            if k not in state_list:
                state_list.append(k)
            else:
                state_list.remove(k)
                left.append(k)
        state_list += left
    
    num = 1
    for el in state_list:
        num *= el
    return num

print(min_evenly_divisible(20))






    