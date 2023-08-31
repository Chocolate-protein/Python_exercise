# practice1 : 자료형, 변수, 주석
# 숫자 자료형 
'''
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3*2)
'''
# 문자형 자료형
'''
print('풍선')
print("나비")
print("ㅋ"*5)
'''

# 명제형 자료형(참/거짓)
'''
print(1 < 2)
print(1 > 2)
print(True)  # 첫글자는 대문자로 해야 인식 o
print(False)
print(not (1 < 2))
'''

# 변수
'''
animal = "고양이"
name = "괭이"
age = 7
hobby = "산책"
is_adult = age >= 4

print("우리집 " + animal + " 이름은 "+ name +"입니다")
# print(name + "는 " + str(age) + "살이고, " + hobby + "을 좋아합니다")
print(name, "는 ", age, "살이고, ", hobby, "을 좋아합니다")
# "+" 사용 : only 문자형,  ","사용 : 숫자형 ok ,but 띄어쓰기 자동 포함
print(name +"는 어른일까요? " + str(is_adult))
# str : 숫자형 -> 문자형으로 표현

age = 10
print(str(age))
'''

# 주석 단축키 : Ctrl + /