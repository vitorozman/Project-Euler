
def dolzina_collatzovo(n):
    sez = []
    while n != 1: 
        sez.append(n)           
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
    return len(sez)


def vsa_zap_do_miljon():
    n = 1
    dolzina_zacetni = {}
    while n != 10 ** 6:
        dolzina_zacetni[dolzina_collatzovo(n)] = n
        n += 1
    return dolzina_zacetni[max(dolzina_zacetni)]

print(vsa_zap_do_miljon())
837799