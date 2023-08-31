# 11721번) 열 개씩 끊어 출력하기

word = input()

while True:
    if len(word) > 10 :
        print(word[:10])
        word = word[10:]
    else:
        print(word)
        break
