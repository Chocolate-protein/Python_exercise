# 10872번) X보다 작은 수

n, x = map(int, input().split())

a = list(map(int, input().split()))
small = []

for i in range(0, len(a)):
    if x > a[i]:
        small.append(a[i])

for i in range(0, len(small)):
    print(int(small[i]), end=" ")