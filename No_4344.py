# 4344번) 평균은 넘겠지

case = int(input())
sum = 0

for _ in range(0, case):
    score = list(map(int, input().split()))
    sum = 0
    count = 0    
    
    for i in score[1:]:   # 평균 구하기
        sum += i
    avg = sum/(len(score)-1)
    
    for j in score[1:]:   # 평균과 비교하기
        if j > avg:
            count += 1
    print("{:.3f}%".format(count/score[0]*100))