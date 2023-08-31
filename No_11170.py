# 11170번) 0의 개수

t = int(input())

for _ in range(0, t):
    n, m = map(int, input().split())
    nums = list(range(n, m+1))
    zeros = list()
    count = 0

    for i in range(0, len(nums)):
        nums[i] = str(nums[i])
        if "0" in nums[i]:
            zeros.append(nums[i])

    for j in zeros:
        if "0" in j:
            count += j.count("0")

    print(count)