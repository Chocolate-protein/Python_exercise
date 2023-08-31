# 9506번) 약수들의 합

while True:
    n = int(input())
    if n == -1:
        break

    fact = []
    for i in range(1, n+1):
        if n%i == 0:
            fact.append(i)

    sum = 0
    for i in range(0, len(fact)-1):
        sum += int(fact[i])

    if sum == n:
        perfect = str(fact[-1]) + " = " + str(fact[0])
        for i in fact[1:-1]:
            perfect += " + " + str(i)
        print(perfect)
    else:
        print("{} is NOT perfect.".format(n))