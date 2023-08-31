# 11655번) ROT13

abc_L = list("abcdefghijklmnopqrstuvwxyz")
abc_U = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
s = list(input())
answer = list()

for i in range(0, len(s)):
    if s[i] in abc_L:
        if abc_L.index(s[i])+13 >= len(abc_L):
            answer.append(abc_L[abc_L.index(s[i])-13])
        else:
            answer.append(abc_L[abc_L.index(s[i])+13])

    elif s[i] in abc_U:
        if abc_U.index(s[i])+13 >= len(abc_U):
            answer.append(abc_U[abc_U.index(s[i])-13])
        else:
            answer.append(abc_U[abc_U.index(s[i])+13])
        
    else:
        answer.append(s[i])

answer = "".join(answer)
print(answer)