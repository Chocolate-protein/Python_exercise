# 2748번) 피보나치 수 2

n = int(input())

fibonacci = [0, 1]

for i in range(1, n):
    next = fibonacci[i] + fibonacci[i-1]
    fibonacci.append(next)

print(fibonacci[-1])
