# 11557번) Yangjojang of The Year


t = int(input())

for i in range(t):
    num = int(input())
    univ1, lit1 = map(str, input().split())
    lit1 = int(lit1)
    for _ in range(num-1):
        univ2, lit2 = map(str, input().split())
        lit2 = int(lit2)
        if lit1 < lit2:
            univ1 = univ2
            lit1 = lit2
    print(univ1)
