# 11653번) 소인수 분해

n = int(input())
divisor = 2

while n != 0:
    if n % divisor == 0:
        n = n/divisor
        print(divisor)
    elif n <= divisor:
        break
    elif n % divisor != 0:
        divisor += 1
    