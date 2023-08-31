# 2309번) 일곱 난쟁이

height = list()

for _ in range(0, 9):
    height.append(int(input()))

num = -100

for i in height:
    num += i

for j in height:
    for k in height:
        if j == k:
            continue
        elif j + k == num:
            height.remove(j)
            height.remove(k)
            break
    if len(height) == 7:
        break

height.sort()

for l in height:
    print(l)