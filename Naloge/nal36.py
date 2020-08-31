
def je_palindrom(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        False

def pretvori_v_binarni(n):
    return int(bin(n).replace('0b', ''))

def sum_palindromov_do(n):
    vsota = 0
    for st in range(1, n + 1):
        if je_palindrom(st) and je_palindrom(pretvori_v_binarni(st)):
            vsota += st
    return vsota

print(sum_palindromov_do(1000000))
872187