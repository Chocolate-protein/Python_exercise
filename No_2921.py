# 2921번) 도미노

n = int(input())
domino = list(range(1, n+1))

sum = 0

for i in domino:
    for j in range(i, i*2 + 1):
        sum += j

print(sum)

'''
1 : 0 1 2 = 3

2 : 0 1 2 / 2 3 4 = 12 

3 : 0 1 2 / 2 3 4 / 3 4 5 6 = 30

4 : 0 1 2 / 2 3 4 / 3 4 5 6 / 4 5 6 7 8 
...

기존 합 + n ~ 2n 까지의 합

'''