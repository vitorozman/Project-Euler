# https://projecteuler.net/problem=31

def f(money, amount):
    if amount <= 0:
        return 1
    if len(money) == 0:
        return 0
    money.sort(reverse=True)
    coin = money[0]
    if coin < amount:
        return f(money, amount-coin) + f(money[1:], amount) if len(money)>1 else f(money, amount-coin)
    elif coin > amount:
        return f(money[1:], amount) if len(money)>1 else 0
    elif coin == amount:
        return 1 + f(money[1:], amount) if len(money)>1 else 1

money = [200, 100, 50, 20, 10, 5, 2, 1]
print(f(money, 200))