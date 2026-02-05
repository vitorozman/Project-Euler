# https://projecteuler.net/problem=17




DICT_NAMES = {
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
    20:'twenty',
    30:'thirty',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety',
    1000:'onethousand'
}

def num_to_word(n):
    """Assume n <= 1000"""
    word = ''
    # hundreds
    n00 = n // 100
    if n00 != 0:
        word += DICT_NAMES[n00] + 'hundred'
        n = int(str(n)[1:])
        if n == 0:
            return word
    # tens
    n0 = n // 10
    if n <= 20:
        return word + 'and' + DICT_NAMES[n] if n00 != 0 else word + DICT_NAMES[n]
    if n0 != 0:
        n = int(str(n)[1:])
        n0 = n0*10
        word += 'and' + DICT_NAMES[n0] if n00 != 0 else DICT_NAMES[n0]
    word += DICT_NAMES[n] if n != 0 else ''
    return word

# print(num_to_word(1))

total_sum = 0
for i in range(1, 1001):
    if i in DICT_NAMES.keys():
        total_sum += len(DICT_NAMES[i])
    else: 
        total_sum += len(num_to_word(i))

print(total_sum)
