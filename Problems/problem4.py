# https://projecteuler.net/problem=4

def is_palindrom(n):
    return str(n) == str(n)[::-1]
       
def max_palindrom(n):
    for i in range(1, n): # tell me the position
        row1 = []
        row2 = []
        num = (n-i + 1)
        for j in range(i):
            calc_num1 = (num-j)*(num+j)
            if is_palindrom(calc_num1):
                row1.append(calc_num1)
            calc_num2 = (num-j)*(num+j+1)
            if is_palindrom(calc_num2):
                row2.append(calc_num2)
        rows = row1+row2
        if len(rows)==0:
            continue
        else:
            return max(rows)
    
print(max_palindrom(999))
# 906609




    