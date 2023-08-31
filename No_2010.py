# 2010번) 플러그
# 입력의 범위가 클경우 input() -> 시간 초과
# => sys 활용 : sys.stdin.readline()

import sys

multitap = int(sys.stdin.readline())

total = -(multitap-1)

for i in range(0, multitap):
    con = int(sys.stdin.readline())
    total += con

print(total)