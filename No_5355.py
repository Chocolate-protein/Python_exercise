# 5335) 화성 수학

T = int(input())

for _ in range(T):
    lst = list(input().split())
    num = float(lst[0])

    for i in range(len(lst)):
        if lst[i] == "@":
            num *= 3
        elif lst[i] == "%":
            num += 5
        elif lst[i] == "#":
            num -= 7

    print("%0.2f" %num)
