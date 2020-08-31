def fakulteta(n):
    if n == 1:
        return 1
    else:
        return fakulteta(n - 1) * n

def binomski_simbol(n, k):
    return fakulteta(n) // (fakulteta(k) * fakulteta(n - k) )


def stevilo_poti(stevilo):
    a = 2 * stevilo
    return binomski_simbol(a, stevilo)
    
print(stevilo_poti(20))
137846528820