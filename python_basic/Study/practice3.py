# #practice2 : 연산자, 수식, 함수
# # 연산자
# print(1+1) # 2
# print(3-2) # 1
# print(5*2) # 10
# print(5/2) # 2.5

# print(2**3) # ** : 제곱 -> 2^3 = 8
# print(2**(-4))

# print(10%3) # 1 (나머지)
# print(10//3) # 3 (몫)



# # 비교 연산자
# print(10 >= 3) # True 
# print(5 == 4) # False 
# print(5 != 4) # True
# print(not (5 == 4)) # True

# print((3 > 0) and (3 <= 1)) # False (and : 둘다 만족)
# print((3 > 0) & (3 <= 1)) # and == &

# print((3 > 0) or (3 <= 1)) # True (or : 하나 이상 만족)
# print((3 > 0) | (3 <= 1)) # or == |

# print(5 > 4 > 3) # True 
# print(5 > 4 > 7) # False 4



# # 수식
# print(2 + 3 * 4) # 14
# print((2 + 3) * 4) # 20
# number = 2 + 3 * 4 # 14
# print(number)

# number = number + 2 # 16
# print(number)
# number += 2 # 18 (== number = number + 2)
# print(number)
# number -=2 # 16
# print(number)
# number *= 2 # 32
# print(number)
# number /= 2 # 16
# print(number)
# number %= 3 # 1
# print(number)



# # 숫자 처리 함수
# print(abs(-5)) # 5                   abs : 절대값
# print(pow(4, 2)) # 2^4 = 16          pow : 제곱
# print(max(13, 34)) # 34              max : (입력값 중)최대값
# print(max(13, 34, 100)) # 100
# print(min(2, 48, 37)) # 2            min : (입력값 중)최소값
# print(round(3.14)) # 3               round : 반올림
# print(round(9.84)) # 10

# from math import * # "math" 라이브러리의 모든것을 이용한다
# print(floor(4.98)) # 4               floor : 내림
# print(ceil(3.14)) # 4                ceil : 올림
# print(sqrt(16)) # 4                  sqrt : 제곱근(루트)



# # 랜덤함수
# from random import *

# print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
# print(random() * 20) # 0.0 ~ 20.0 미만의 임의의 값 생성

# print(int(random() * 20)) # 0 ~ 20 미만의 임의의 정수값 생성
# print(int(random() * 45) + 1) # 1 ~ 46 미만의 임의의 정수값 생성
# print(int(random() * 7) - 5) # -5 ~ 2 미만의 값

# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 정수값 생성

# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 정수값 생성