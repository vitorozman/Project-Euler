def prvo_tisoc_mestno_fibonacijevo():
    a = 1
    b = 1
    index = 2
    while len(str(b)) < 1000:
        c = a
        a = b
        b = b + c
        index += 1
    return index

print(prvo_tisoc_mestno_fibonacijevo())
4782