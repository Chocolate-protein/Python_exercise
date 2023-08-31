# A+B  -  7

i = int(input())
count = 1

while i > 0:
    a, b = map(int, input().split())
    sum = a+b
    print("Case #{0}: {1}".format(count, sum))
    count += 1
    i -= 1