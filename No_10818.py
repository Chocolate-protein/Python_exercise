# 10818번) 최소, 최대

n = int(input())

data = list(map(int, input().split()))
lst = [0] * n

for i in range(0, n):
    lst[i] = data[i]

lst.sort()
print(lst[0], lst[-1])