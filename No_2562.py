# 2562번) 최댓값

nums = []
max_num = 0

for i in range(0,9):
    n = int(input())
    nums.append(n)

    if n > max_num:
        max_num = n

print(max_num)
print(nums.index(max_num)+1)

'''
lst = []
max = [0] * 9

for i in range(0, 9):
    lst.append(int(input()))
    max[i] = 100 - lst[i]

max.sort()
m = lst.index(100-max[0]) + 1

print(lst[m-1])
print(m)
'''