#  2746번) 주사위 게임

n = int(input())
win = list(range(0, n))

def compare(*num):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b: 
        return c


for i in range(n):
    a, b, c = map(int, input().split())
    if a == b == c:
        win[i] = 10000 + a * 1000
    elif a == b != c or a == c != b:
        win[i] = 1000 + a * 100
    elif b == c != a:
        win[i] = 1000 + b * 100
    else:
        win[i] = compare(a, b, c) * 100

win.sort()
print(win[n-1])
