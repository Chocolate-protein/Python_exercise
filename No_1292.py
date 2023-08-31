# 1292번) 쉽게 푸는 문제

n1, n2 = map(int, input().split())
sum = 0

num_list = list()
for i in range(1, n2*2):
    for j in range(0, i):
        num_list.append(i)

for k in num_list[n1-1:n2]:
    sum += k

print(sum)