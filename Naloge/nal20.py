import math as m

def vsota_stevk_fakultete(n):
    vsota = 0
    for stevka in str(m.factorial(n)):
        vsota += int(stevka)
    return vsota

print(vsota_stevk_fakultete(100))
648