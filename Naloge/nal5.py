def min_deljiv_z(a, b):
    stevilo = 19 * 19 #manse od tega nemore biti
    while True:
        vsa_st = set()
        for x in range(a, b + 1):
            if stevilo % x == 0:
                vsa_st.add(x)
                continue
            else:
                break
        if len(vsa_st) == b:
            return stevilo 
        stevilo += 1        

print(min_deljiv_z(1, 20))#rabi nekaj casa
232792560