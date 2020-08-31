def je_prestopno(leto):
    return  leto % 4 == 0 and leto % 100 != 0 or leto % 400 == 0
            
def stevilo_dni(mesec, leto): 
    if mesec == '1' or mesec == '3' or mesec == '5' or mesec == '7' or mesec == '8' or mesec == '10' or mesec == '12':
       return 31
    elif mesec == '4' or mesec == '6' or mesec == '9' or mesec == '11' :
        return 30
    elif mesec == '2' and je_prestopno(leto):
        return 29
    else: 
        return 28  

def presteje_sobote():
    dnevi = ['Tus','Wed','Thu','Fry','Sat','Sun','Mon']
    meseci = ['1','2','3','4','5','6','7','8','9','10','11','12']
    leta = [i for i in range(1901,2001)]
    
    seznam_dni_ki_so_ze_mimo = []
    seznam_prvih_v_mesecu = []
    je_prvi_v_mesecu = True
    for leto in leta:
        for mesec in meseci:
            je_prvi_v_mesecu = True
            for _ in range(stevilo_dni(mesec, leto)):
                if je_prvi_v_mesecu:
                    seznam_prvih_v_mesecu.append(dnevi[0])
                    je_prvi_v_mesecu = False
                seznam_dni_ki_so_ze_mimo.append(dnevi[0])
                dnevi.append(dnevi.pop(0))
    sestej = 0
    for i in seznam_prvih_v_mesecu:
        if  i == 'Sun':
            sestej += 1
    return sestej

print(presteje_sobote())
171
