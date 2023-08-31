# 10988번) 팰린드롬인지 확인하기

# 풀이1
word = list(str(input()))

if list(reversed(word)) == word:
    print(1)
else:
    print(0)

# 풀이2(내가 푼거)
'''
word = input().lower()
word = list(word)

ex = [0] * len(word)

e = 0
o = 0

if len(word)%2 == 0:   # 짝수개
    while e < len(word)/2:
        if word[e] == word[len(word)-1-e]:
            word[e] = 0
            word[len(word)-1-e] = 0
            
            if word == ex:
                print(1)
                break

        elif word[e] != word[len(word)-1-e]:
            print(0)
            break

        e += 1

else:
    word[int(len(word)/2-0.5)] = 0
    while o <= len(word)/2:
        if word[o] == word[len(word)-1-o]:
            word[o] = 0
            word[len(word)-1-o] = 0

            if word == ex:
                print(1)
                break
        
        elif word[o] != word[len(word)-1-o]:
            print(0)
            break

        o += 1
'''