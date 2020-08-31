
def f(x):
    s = []
    for stevilo in range(1, x):
        if stevilo % 3 == 0 or stevilo % 5 == 0:
            s.append(stevilo)
    return sum(s) 

print(f(1000))
233168