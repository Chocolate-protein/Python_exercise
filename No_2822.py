# 2822번) 점수 계산

score = list()
num_list = list()

for i in range(0, 8):
    score.append(int(input()))
    num_list.append(score[i])

num_list.sort()
num_list = num_list[3:]
sum = sum(num_list)

for j in range(0, len(num_list)):
    num_list[j] = score.index(num_list[j]) + 1

num_list.sort()

print(sum)
for k in num_list:
    print(k, end=" ")