# 4101번) 크냐?

while True:
    num1, num2 = map(int, input().split())
    if num1 == 0 and num2 == 0:
        break
    elif num1 > num2:
        print("Yes")
    else:
        print("No")
