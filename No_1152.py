# 1152번) 단어의 개수
'''
string = input()

if string[0] == " " and string[-1] == " ":
    count = -1
    for i in string:
        if i == " ":
            count += 1
elif string[0] == " " or string[-1] == " ":
    count = 0
    for i in string:
        if i == " ":
            count += 1
else:
    count = 1
    for i in string:
        if i == " ":
            count += 1

print(count)
'''

word = input().split()
print(len(word))