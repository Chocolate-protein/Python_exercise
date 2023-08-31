# 5622번) 다이얼
'''
dial = list(input().lower())

sec = 0

for i in dial:
    if i == 'a' or i == 'b' or i == 'c':
        sec += 3
    elif i == 'd' or i == 'e' or i == 'f':
        sec += 4
    elif i == 'g' or i == 'h' or i == 'i':
        sec += 5
    elif i == 'j' or i == 'k' or i == 'l':
        sec += 6
    elif i == 'm' or i == 'n' or i == 'o':
        sec += 7
    elif i == 'p' or i == 'q' or i == 'r' or i == 's':
        sec += 8
    elif i == 't' or i == 'u' or i == 'v':
        sec += 9
    elif i == 'w' or i == 'x' or i == 'y' or i == 'z':
        sec += 10
    else:
        sec += 11

print(sec)
'''

dial = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

number = list(input().lower())

sec = 0

for n in number:
    for d in dial:
        if n in d:
            sec += dial.index(d) + 3
            break
print(sec)