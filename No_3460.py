# 3460번) 이진수

t = int(input())
for _ in range(0, t):
    n = int(input())
    binary = bin(n)
    binary = list(binary[2:])

    for i in range(0, len(binary)):
        if binary[i] == "1":
            print(binary.index("1"), end=" ")
            binary[i] = "0"   


'''
t = int(input())

for _ in range(0, t):
    n = int(input())

    bit = list()

    while True:
        bit.append(n%2)
        n = n//2
        if n == 1:
            bit.append(n)
            break

    bit.reverse()

    for i in range(0, len(bit)):
        if bit[i] == 1:
            print(bit.index(1), end=" ")
            bit[i] = 0    
'''

# 답 풀이 (문제 이상함)
'''
def binary(n):
    i = 0
    while n != 0:
        if n%2 == 1:
            print(i, end=" ")
        n //= 2
        i += 1

t = int(input())

for _ in range(0, t):
    n = int(input())
    binary(n)
    print()
'''