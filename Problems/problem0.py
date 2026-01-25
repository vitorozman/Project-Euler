def is_odd(n):
    return n % 2 != 0

odd_square_sum = 0
for n in range(1, 192000):
    n2 = n ** 2
    if is_odd(n2):
        odd_square_sum += n2

print(odd_square_sum)
# 1179647999968000