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


def st_deliteljev(n):
    return len([x for x in delitelji(n)])


def iskani_clen(n):
    k = 0
    st = st_deliteljev(k)
    stevec = 0
    while st < n:
        stevec += 1
        k += stevec
        st = st_deliteljev(k) 
    return k

iskani_clen(500) #rabi nekaj casa
76576500