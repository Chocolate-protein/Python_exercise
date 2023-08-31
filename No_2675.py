# 2675번) 문자열 반복

'''
1 : 케이스 반복횟수 개수
2 : 
'''
'''
t = int(input())

for _ in range(t):
    s = list(input())
    r = int(s[0])
    s = s[2:]
    p = list()
    for i in range(len(s)):
        p = s[i]*r
        print(p, end='')
    print()
'''

t = int(input())

for i in range(0, t):
    r, s = map(str, input().split())
    r = int(r)

    for j in s:
        print(j*r, end="")
    print()