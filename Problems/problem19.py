# https://projecteuler.net/problem=19

def zellerCongruence(date, show=False):
    q, m, y = map(int, date.split())  # day, month, year

    if m < 3:   
        m += 12
        y -= 1

    k = y % 100  # yearpart
    j = y // 100 # century

    h = (q + (13 * (m + 1)) // 5 + k + k // 4 + j // 4 + 5 * j) % 7  
    if show:
        wd = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        return wd[h]
    else:
        return h
        
count_sundays = 0
for year in range(1901, 2001):
    for month in range(1, 12+1):
        if zellerCongruence(f'{1} {month} {year}') == 1:
            count_sundays += 1
print(count_sundays)
