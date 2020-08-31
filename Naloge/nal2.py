def vsota_sodih_fibonaccijevih_clenov_majnsih_od(n):
    a = 1
    b = 2
    s = []
    while b <= n:
        if b % 2 == 0:
            s.append(b)
        c = a
        a = b
        b = c + a
    return sum(s)

print(vsota_sodih_fibonaccijevih_clenov_majnsih_od(4000000))
4613732