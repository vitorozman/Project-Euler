
slovar = {'A' : 1,'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10, 'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26}

def pretvori_in_sortiraj(ime_datoteke):
    with open(ime_datoteke, encoding='UTF-8') as dat_imena:
        imena = dat_imena.read().replace('"', '')
        imena = imena.split(',')
    imena.sort()
    return imena

def skupni_sestevek(ime_datoteke, slovar):
    vsota = 0
    sez_imen = pretvori_in_sortiraj(ime_datoteke)
    for ime in sez_imen:
        ste = 0
        for znak in ime:
            ste += slovar[znak]
        vsota += (sez_imen.index(ime) + 1) * ste
    return vsota

print(skupni_sestevek('IMENA.txt', slovar))
871198282