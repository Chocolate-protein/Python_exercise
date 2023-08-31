# 1357번) 뒤집힌 덧셈

def Rev(x):
    x = list(str(x))
    x.reverse()
    word = ""
    for i in x:
        word += i
    return int(word)

x, y = map(int, input().split())

print(Rev(Rev(x) + Rev(y)))