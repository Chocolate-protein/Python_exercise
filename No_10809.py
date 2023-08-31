# 10809번) 알파벳 찾기
'''
from string import ascii_lowercase

s = input()

ind = list()
alphabet = list(ascii_lowercase)

for i in alphabet:
    if i in s:
        ind.append(s.index(i))
    else:
        ind.append(-1)

for j in ind:
    print(j, end=" ")
'''

# if 문에도 'in' 사용 가능

abc = list("abcdefghijklmnopqrstuvwxyz")
s = list(input())

for i in abc:
    if i in s:
        print(s.index(i), end=" ")
    else:
        print(-1, end=" ")