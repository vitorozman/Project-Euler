slovar_stevil_z_besedo = {
    0 : '',
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen',
    20 : 'twenty',
    30 : 'thirty',
    40 : 'forty',
    50 : 'fifty',
    60 : 'sixty',
    70 : 'seventy',
    80 : 'eighty',
    90 : 'ninety', 
    100 : 'onehundred',
    200 : 'twohundred',
    300 : 'threehundred', 
    400 : 'fourhundred',
    500 : 'fifehundred',
    600 : 'sixhundred',
    700 : 'sevenhundred',
    800 : 'eighthundred',
    900 : 'ninehundred',
    1000 : 'onethousand'
}


def vsota_crk_stevil_do(n=1000):
    vsota = 0
    for st in range(1, n+1):
        if st in slovar_stevil_z_besedo:
            vsota += len(slovar_stevil_z_besedo[st])
        elif st < 100:
            besede = slovar_stevil_z_besedo[int(str(st)[0]) * 10] + slovar_stevil_z_besedo[st % 10]
            vsota += len(besede)
        elif st < 1000:
            stotice = slovar_stevil_z_besedo[int(str(st)[0]) * 100] + 'and'
            if st % 100 < 20:
                ostalo = slovar_stevil_z_besedo[st % 100]
            else:
                ostalo = slovar_stevil_z_besedo[int(str(st)[1]) * 10] + slovar_stevil_z_besedo[st % 10]
            beseda = stotice + ostalo
            vsota += len(beseda)
    return vsota


print(vsota_crk_stevil_do(1000))
21124