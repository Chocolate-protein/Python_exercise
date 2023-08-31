# 11098번) 첼시를 도와줘!

n = int(input())

for i in range(0, n):
    p = int(input())
    salay = 0
    for j in range(0, p):
        c, name = map(str, input().split())
        if int(c) > salay:
            salay = int(c)
            player = name
        
    print(player)