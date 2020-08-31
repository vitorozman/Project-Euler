def vsota_stevk_potence_z_osnovo_dve(k=1000):
    stevilo = 2 ** k
    vsota = 0
    for stevka in str(stevilo):
        vsota += int(stevka)
    return vsota

print(vsota_stevk_potence_z_osnovo_dve(1000))
1366