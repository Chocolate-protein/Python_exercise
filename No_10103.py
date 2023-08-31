# 10103번) 주사위 게임

n = int(input())

Chang = 100
Sang = 100

for _ in range(n):
    num_C, num_S = map(int, input().split())
    if num_C > num_S:
        Sang = Sang - num_C
    elif num_C < num_S:
        Chang = Chang - num_S

print(Chang)
print(Sang)