# 5800번) 성적 통계

case = int(input())
for i in range(0, case):
    score = list(map(int, input().split()))
    score = score[1:]
    score.sort()
    gap = 0
    for j in range(1, len(score)):
        if score[j]-score[j-1] > gap:
            gap = score[j] - score[j-1]
    
    print("Class {}".format(i+1))
    print("Max {}, Min {}, Largest gap {}".format(max(score), min(score), gap))