# 1065번) 한수
'''
n = int(input())

def hansu(n):
    n = str(n)
    count = 0
    if len(n) == 1 or len(n) == 2:
        count = int(n)
        return count
    elif len(n) >= 3:
        for _ in range(100, int(n)+1):
            n = str(n)
            if int(n[1]) - int(n[0]) == int(n[2]) - int(n[1]):
                count += 1
            n = int(n)-1
        return count+99

print(hansu(n))
'''

def hansu(n):
    count = 0
    for i in range(1, n+1):
        num_list = list(map(int, str(i)))
        if i < 100:
            count += 1
        elif num_list[0] - num_list[1] == num_list[1] - num_list[2]:
            count += 1
    return count

number = int(input())
print(hansu(number))
