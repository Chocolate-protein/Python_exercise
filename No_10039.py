# 10039번) 평균점수
'''
students = [True] * 5
i = 0

while i < 5:
    students[i] = int(input())
    if int(students[i]) < 40:
        students[i] = 40
    i += 1

j = 1

while j < 5:
    students[j] = int(students[j-1]) + int(students[j])
    j += 1
    
print(int(students[4])//5)
'''
## "/" 연산자 -> 실수형 출력,  "//"연산자 -> 정수형 출력

# 원래 풀이
'''
total = 0

for i in range(5):
    tmp = int(input())

    if tmp < 40:
        tmp = 40
    
    total += tmp

print(total//5)
'''

# 추가 풀이(다시)

total = 0

for i in range(1, 5+1):
    score = int(input())
    if score >= 40:
        total += score
    else:
        total += 40
print(total//5)