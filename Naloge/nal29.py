#vse mozne kombinacije a**b za 2 <= a <= 100 enak za b

def vse_kombinacije(od, do):
    sez_kombinacij = []
    for osnova in range(od, do + 1):
        for potenca in range(od, do + 1):
            if osnova ** potenca not in sez_kombinacij:
                sez_kombinacij.append(osnova ** potenca)
    return len(sez_kombinacij)

print(vse_kombinacije(2, 100))
9183