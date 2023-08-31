# 11022) A+B   -   8

i = int(input())
count = 1

while i > 0:
    a, b = map(int, input().split())
    sum = a+b
    print("Case #{0}: {1} + {2} = {3}".format(count, a, b, sum))
    count += 1
    i -= 1



# # 풀이 2
# for count in range(1, i+1):
#     a, b = map(int, input().split())
#     sum = a+b
#     print("Case #{0}: {1} + {2} = {3}".format(count, a, b, sum))
#     count += 1