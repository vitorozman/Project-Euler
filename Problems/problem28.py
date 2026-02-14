# https://projecteuler.net/problem=28


def sum_of_diag(n=1001):
    
    step = 2
    current_sum = 1
    num_list = [i for i in range(1, n*n+1)]
    i = 0
    loops = int((n-1)/2)
    for _ in range(loops):
        for s in range(1, 4+1):
            index = i + s*step
            print(index)
            current_sum += num_list[index]
        i = index
        step += 2
    
    return current_sum

print(sum_of_diag(1001))