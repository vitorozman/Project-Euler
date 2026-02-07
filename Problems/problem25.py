# https://projecteuler.net/problem=25



def find_1000_digit_fibonaci():
    fibonacci_seq = [1, 1]
    i = 2
    while len(str(fibonacci_seq[-1]))<1000:
        i +=1
        fibonacci_seq.append(fibonacci_seq[-1]+fibonacci_seq[-2])
    return len(fibonacci_seq)

print(find_1000_digit_fibonaci())