# 1978번) 소수 찾기

n = int(input())

nums = list(map(int, input().split()))

prime = []

def find_prime(num1):
    for i in range(2, num1):
        if num1%i == 0:
            return False
    return True

for j in nums:
    if j == 2:
        prime.append(2)

    elif find_prime(j):
        prime.append(j)

if 1 in prime:
    prime.remove(1)
     
print(len(prime))