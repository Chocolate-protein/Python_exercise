# 10102번) 개표

v = int(input())
a = 0
b = 0

vote = map(str, input())
vote = list(vote)

while v >= 1:
    if vote[v-1] == "A":
        a += 1
    elif vote [v-1] == "B":
        b += 1
    v -= 1

if a > b:
    print("A")
elif a < b:
    print("B")
else:
    print("Tie")
