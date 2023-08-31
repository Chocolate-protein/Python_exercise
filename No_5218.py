# 5218번) 알파벳 거리

case = int(input())
abc = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
nums = list(range(1, 27))

for _ in range(0, case):
    w1, w2 = map(str, input().split())
    distance = list()

    for i in range(0, len(w1)):
        if nums[abc.index(w1[i])] <= nums[abc.index(w2[i])]:
            distance.append(nums[abc.index(w2[i])] - nums[abc.index(w1[i])])
        elif nums[abc.index(w1[i])] > nums[abc.index(w2[i])]:
            distance.append(nums[abc.index(w2[i])] - nums[abc.index(w1[i])] + 26)

    print("Distances: ", end="")
    for j in distance:
        print(j, end=" ")
    print()