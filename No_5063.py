# 5063번) TGN

n = int(input())

for _ in range(n):
    r, e, c = map(int, input().split())
    benefit = e - c
    if benefit > r:
        print("advertise")
    elif benefit < r:
        print("do not advertise")
    elif benefit == r:
        print("does not matter")
