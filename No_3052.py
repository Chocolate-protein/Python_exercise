# 3052번) 나머지

num = []

for i in range(0, 10):
    num.append(int(input()))
    num[i] = int(num[i])%42

num = set(num)
print(len(num))