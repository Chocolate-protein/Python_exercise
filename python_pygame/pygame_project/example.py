# 1. enumerate(list)
'''
lst = ["가", "나", "다"]

for i, j in enumerate(lst):
    print(i, j)
'''

# 2. 이중 반복문 탈출
balls = [1, 2, 3, 4]
weapons = [11, 22, 3, 44]

for ball_idx, ball_val in enumerate(balls):
    print("ball :", ball_val)
    for weapon_idx, weapon_val in enumerate(weapons):
        print("weapons :", weapon_val)
        if ball_val == weapon_val:   # 충돌 체크
            print("공과 무기가 충돌")
            break                 #  ㅡㅡㅡㅡㅡㅡㅡㅡ   break => else 건너뜀
    else:   # 반복할 내용이 없으면 else 동작        |
        continue                  #                |
    print("바깥 for 문 break")    #                |
    break      #  <ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ-