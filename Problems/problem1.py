# https://projecteuler.net/problem=1

n = 1000
total = 0
for i in range(n):
    if i % 3 == 0:
        total += i
    elif i % 5 == 0:
        total += i
print(total)
# 233168
