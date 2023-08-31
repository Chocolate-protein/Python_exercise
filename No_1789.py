# 1789번) 수들의 합


sum1 = int(input())

num = 0

while True:
    sum1 = sum1 - num
    num += 1
    if num > sum1:
        print(num-1)
        break
        

