def vskota_vadratov(n):
    vsota = 0
    for st in range(1, n + 1):
        vsota += st ** 2
    return vsota

def kvadrat_vsote(n):
    vsota = 0
    for st in range(1, n + 1):
        vsota += st
    return vsota ** 2

def razlika(n):
    return kvadrat_vsote(n) - vskota_vadratov(n)