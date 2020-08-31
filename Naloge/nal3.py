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
    kandidat = n + 1
    while not je_prastevilo(kandidat):
        kandidat += 1
    return kandidat

def najvecje_prastevilo_stevia(n):
    p = []
    trenutno = 1
    while n > trenutno:
        if n % trenutno == 0:
            p.append(trenutno)
        trenutno = naslednje_prastevilo(trenutno)
    return max(p)

def eratostenovoReseto(n):
    veckratniki=[]
    prastevila=[]
    for i in range(2,n+1):
        if i not in veckratniki:
            prastevila.append(i)
            for j in range(i*i, n+1, i):
                veckratniki.append(j)
    return prastevila

def poskusnoDeljenje(n):
    kandidati= eratostenovoReseto(n) # seznam kandidatov
    prafaktorji=[] # seznam, v katerem bojo prafaktorji števila n
    ix=0 # indeks trenutnega kandidata v seznamu
    while n>1:
        # če kandidat deli n, potem ga dodamo v seznam,
        # vrednost n pa delimo s tem prafaktorjem
        if n%kandidati[ix]==0: 
            prafaktorji.append(kandidati[ix])
            n//=kandidati[ix]
        # sicer povečamo indeks
        else:
            ix+=1
    return max(prafaktorji)

from math import *


def fermat(n, sez=None):
    '''Za dan n vrne seznam njegovih prafaktorjev'''
    if sez==None:
        sez=[]
    # ustavitveni pogoji
    if n==1: return sez
    # če je število sodo, ga delimo toliko časa, dokler lahko
    if n%2==0:
        sez.append(2)
        fermat(n//2,sez)
        return sez
    else:
        # fermatov algoritem
        # izračunamo vrednosti x in y
        x=ceil(sqrt(n))
        y=x**2-n
        while sqrt(y)%1!=0: # dokler y ni popoln kvadrat
            x+=1 # povečujemo x
            y=x*x-n # poračunamo y, ki bi ustrezal x-u
        a=x-sqrt(y)
        b=x+sqrt(y)
        # če je kateri od faktorjev števila 1, potem je drugi praštevilo
        if a==1:
            sez.append(int(b))
            return sez
        if b==1:
            sez.append(int(a))
            return sez
        # na koncu rekurzivno pokličemo funkcijo na obeh faktorjih
        # in izračunamo njune prafaktorje
        fermat(a,sez)
        fermat(b,sez)        
        return max(sez)


fermat(600851475143)

