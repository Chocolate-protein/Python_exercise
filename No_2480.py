# 2480번) 주사위 세개

a, b, c = map(int, input().split())
prize = 0

def compare(*num):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c

if a == b == c:
    prize = 10000 + a * 1000
elif a == b or a == c:
    prize = 1000 + a * 100
elif b == c:
    prize = 1000 + b * 100
else:
    prize = compare(a, b, c)
    prize = 100 * prize

print(prize)