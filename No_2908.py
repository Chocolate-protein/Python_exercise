# 2908번) 상수

a, b = map(str, input().split())

a_r = int(a[::-1])
b_r = int(b[::-1])

if a_r > b_r:
    print(a_r)
else:
    print(b_r)

# 문자열 뒤집기
# : a[::-1]