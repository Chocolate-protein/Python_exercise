# 10991번) 별 찍기 - 16

n = int(input())

for i in range(1, n+1):
    star = (("* "*i).rstrip(" ")).center(2*n - 1, " ")
    print(star.rstrip(" "))