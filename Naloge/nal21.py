def delitelji(n):
    d = []
    i = 1
    while i**2 < n:
        if n % i == 0:
            yield i
            d.append(n // i)
        i += 1
    if i**2 == n:
        yield i
    while len(d) > 0:
        yield d.pop()

def d(n):
    s = [x for x in delitelji(n)]
    if len(s) >= 2:
        s = s[:-1]
    return sum(s)


def prijateljska_stevila_do(n=10000):
    sez_prijateljev = []
    for stevilo in range(1, n + 1):
        b = stevilo
        a = d(b)
        if d(a) == b and a != b:
            sez_prijateljev.append(stevilo)
    return sum(sez_prijateljev)

print(prijateljska_stevila_do(10000))
31626