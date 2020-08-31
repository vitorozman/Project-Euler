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

def naslednje_prastevilo(n):
    n += 1
    while True:
        if je_prastevilo(n):
            return n
        n += 1

def vsota_prastevil_mnjsa_od(n):
    prastevilo = 2
    sez = []
    while prastevilo <= n:
        sez.append(prastevilo)
        prastevilo = naslednje_prastevilo(prastevilo)
    return sum(sez)