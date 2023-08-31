# from ipaddress import NetmaskValueError


# Quiz 3) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예)http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성

# 예) 생성된 비밀번호 : nav51!

# # 방법 1
# adr = "http://youtube.com"
# password = adr[7:-4] # naver

# print("생성된 비밀번호 " + password[:3] + str(len(password)) + str(password.count("e")) + "!")


# # 방법 2
# adr = "http://youtube.com"
# rule = adr.replace("http://", "") # 규칙1
# rule = rule[:rule.index(".")] # 규칙2
# p1 = rule[:3]
# p2 = len(rule)
# p3 = rule.count("e")
# password = p1 + str(p2) + str(p3) + "!"

# print(f"생성된 비밀번호 : {password}")
# print("{0} 의 비밀번호는 \"{1}\" 입니다.".format(adr, password))
