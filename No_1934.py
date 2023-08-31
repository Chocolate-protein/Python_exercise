# 1934번) 최소공배수

from math import *

case = int(input())

for i in range(case):
    x, y = map(int, input().split())
    print(lcm(x, y))

"""
-- 유클리드 호제법(최대공약수 구하기) --
ex) 1071과 1029의 최대공약수
1071은 1029로 나누어 떨어지지 않기 때문에, 1071을 1029로 나눈 나머지를 구한다. ≫ 42
1029는 42로 나누어 떨어지지 않기 때문에, 1029를 42로 나눈 나머지를 구한다. ≫ 21
42는 21로 나누어 떨어진다.
따라서, 최대공약수는 21이다.


코드 : math -> gcd(x, y)

def gcd(x, y):
    while y:
        x, y = y, x%y
    return x


--- 최소공배수 구하기 ---
두 값을 곱한 후 최대공약수로 나눈다
 
코드 : math -> lcm(x, y)

def lcm(x, y):
    return x * y // gcd(x, y)

"""