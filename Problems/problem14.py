# https://projecteuler.net/problem=14

long_chain = 0
num = -1 
memory_chain = {1 : 1}

def countChain(n):
    if n in memory_chain:
        return memory_chain[n]
    elif n % 2 == 0:
        memory_chain[n] =  1 + countChain(int(n/2))
    else: 
        memory_chain[n] =  2 + countChain(int((3*n + 1)/2))
    
    return memory_chain[n]

for i in range(5*10**5, 10**6):
    count_chain = countChain(i)
    if count_chain > long_chain:
        long_chain = count_chain
        num = i
print(num, long_chain)

