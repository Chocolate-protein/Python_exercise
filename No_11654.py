# 11655번) 아스키 코드

s = input()

if type(s) == str:
    print(ord(s))

elif type(s) == int:
    print(chr(s))

'''
ord(문자) : 아스키 코드 반환
chr(숫자) : 숫자에 맞는 아스키 코드 반환
'''