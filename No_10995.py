# 10995번) 별찍기 - 20

n = int(input())

for i in range(1, n+1):
    if i%2 == 1:
        ans = "* "*n
        ans.rstrip(" ")
    else:
        ans = " *"*n
    print(ans)