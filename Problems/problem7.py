# https://projecteuler.net/problem=7


from useful_functions.prime_numbers import is_prime

def gen_list_of_prime_length(n):
    list_prime = []
    k = 1
    while len(list_prime) <= n:
        if is_prime(k):
            list_prime.append(k)
        k +=1
    return list_prime

print(gen_list_of_prime_length(10001)[-1])

        
