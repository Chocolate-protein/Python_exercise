# 2577번) 숫자으 개수
'''
a = int(input())
b = int(input())
c = int(input())

comp = str(a * b * c)
comp = list(comp)

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
count = [0] * 10

for s in comp:
    i = 0
    while i < 10:
        if int(s) == int(num[i]):
            count[num[i]] += 1
            break
        i += 1

for j in count:
    print(j)
'''

a = int(input())
b = int(input())
c = int(input())

comp = str(a*b*c)

for i in range(0, 10):
    print(comp.count(str(i)))