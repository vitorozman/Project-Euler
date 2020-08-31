
def vsota_diagonal(velikos_matrike):#razprl bom kacasto matriko in dobil neko zap. stevil
    clen = 1
    vsota = 1
    preskoci = 2
    while clen < velikos_matrike ** 2:
        for _ in range(4):
            clen += preskoci
            vsota += clen
        preskoci += 2
    return vsota

print(vsota_diagonal(1001))
669171001