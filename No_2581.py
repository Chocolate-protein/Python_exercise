# 2581번) 소수 : 1978번 참고

m = int(input())
n = int(input())

nums = list(range(m, n+1))

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

prime.sort()
sum = 0
for k in prime:
    sum += k

if len(prime):
    print(sum)
    print(prime[0])
else:
    print(-1)