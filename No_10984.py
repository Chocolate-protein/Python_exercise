# 10984번) 내 학점을 구해줘

sem = int(input())

for _ in range(0, sem):
    sub = int(input())
    sum_c = 0
    sum_g = 0
    for i in range(0, sub):
        cre, grade = map(str, input().split())
        cre = int(cre)
        grade = float(grade)
        sum_c += cre
        sum_g += cre*grade
        avg = round(sum_g / sum_c, 1)
    print("{} {}".format(sum_c, avg))