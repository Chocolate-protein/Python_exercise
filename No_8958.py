# 8958번) OX퀴즈
'''
n = int(input())

for i in range(n):
    test = list(input())
    # print(test)
    add = 0
    score = 0
    j = 0

    while j < len(test):
        add += 1
        if test[j] == "O":
            score += add
        elif test[j] == "X":
            add = 0
        # print("{} 번째 루틴 {}".format(j, score))
        j += 1
    
    # print("최종점수 : {}".format(score))
    print(score)
'''

case = int(input())

for _ in range(0, case):
    
    quiz = list(input())
    sum = 0
    score = 0

    for i in quiz:
        if i == "O":
            sum += 1
            score += sum
        else:
            sum = 0
    
    print(score)