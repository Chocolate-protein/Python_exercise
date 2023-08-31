# 1546번) 평균

n = int(input())
score = list(map(int, input().split()))
score = score[0:n]

m = max(score)
sum = 0

for i in score:
    i = i/m * 100
    sum += i

print(sum/n)
