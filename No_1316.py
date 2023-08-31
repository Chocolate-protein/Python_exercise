# 1316번) 그룹 단어 체커

n = int(input())
count = n

for i in range(0, n):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] != word[j+1]:
            if word[j] in word[j+1:]:
                count -= 1
                break
            else:
                pass

print(count)