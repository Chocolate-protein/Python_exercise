# 1157번) 단어 공부

from string import ascii_uppercase

word = input()
word = word.upper()
alpha = list(ascii_uppercase)
count = [0] * 26

for i in word:
    for j in range(0, len(alpha)):
        if i == alpha[j]:
            count[j] += 1

count_sort = sorted(count)  # 원본은 그대로 두고 싶을 때 : sorted()

if count_sort[-1] == count_sort[-2]:
    print("?")
else:
    print(alpha[(count.index(max(count)))])

'''
abc = list("abcdefghijklmnopqrstuvwxyz")
count = list()
word = input()
word = word.lower()

for i in range(0, len(abc)):
    count.append(word.count(abc[i]))

if count.count(max(count)) > 1 or max(count) == 0:
    print("?")
else:
    m = abc[count.index(max(count))]
    m = m.upper()
    print(m)
'''