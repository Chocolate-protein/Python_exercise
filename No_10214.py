# 10214번) Baseball

t = int(input())

for i in range(1, t+1):
    score_y = 0
    score_k = 0

    for _ in range(1, 9+1):
        y, k = map(int, input().split())
        score_y += y
        score_k += k
    
    if score_k > score_y:
        print("Korea")
    elif score_k < score_y:
        print("Yonsei")
    else:
        print("Draw")
