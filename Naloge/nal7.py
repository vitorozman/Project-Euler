def je_prastevilo(n):
    if n <= 2:
        return n == 2
    elif n % 2 == 0:
        return False
    else:
        d = 3
        while d ** 2 <= n:
            if n % d == 0:
                return False
            d += 2
        return True


def generator_prastevil():
    n = 2
    while True:
        if je_prastevilo(n):
            yield n
        n += 1


g = generator_prastevil()
s = [next(g) for i in range(10001)]
s[-1]
104743
   