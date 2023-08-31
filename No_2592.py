# 2592번) 대표값
nums = list()

for _ in range(0, 10):
    nums.append(int(input()))

sum = 0
count = 0
max = 0
for i in nums:
    sum += i
    if nums.count(i) > count:
        count = nums.count(i)
        max = i

print(sum//10)
print(max)

'''
nums = list()

for _ in range(0, 10):
    nums.append(int(input()))

# 평균
sum = 0
for i in nums:
    sum += i

print(sum//10)

#최빈값
copy = nums
copy = list(set(copy))
count_list = []

for j in copy:
    count = 0
    for k in nums:
        if j == k:
            count += 1
    count_list.append(count)

print(copy[count_list.index(max(count_list))])
'''