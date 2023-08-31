# 10156번) 과자

price, num, money = map(int, input().split())

snack = price * num

if money >= snack:
    print(0)
else:
    print(snack - money)