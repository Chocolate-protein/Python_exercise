# 2711번) 오타맨 고창영

t = int(input())

for i in range(0, t):
    n, s = map(str, input().split())
    n = int(n)
    word = s[:n-1] + s[n:]
    print(word)