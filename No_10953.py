# 10953번) A + B  - 6

case = int(input())

for _ in range(0, case):
    n1, n2 = map(int, input().split(","))
    print(n1 + n2)

# .split() : ()에 " " (공백)이 생략되어 있다.
# 다른 구분자 사용시 넣기
# ex .split(", ")