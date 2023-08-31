# # 문자열
# sentence = 'python basic'
# print(sentence)
# sentence2 = "basic is easy"
# print(sentence2)

# sentence3 = """
# python basic
# and basic is easy
# """
# print(sentence3)



# # 슬라이싱
# pn = "980803-1234567"

# print("성별 : " + pn[7])   # ab[n] -> ab 문자열의 n번째 문자 출력
# print("출생년도 : " + pn[0:2]) # ab[n:m] -> ab문자열의 n ~ (m-1)번째 문자 출력
# print("출생일 : " + pn[2:6])

# print("생년월일 : " + pn[:6]) # ab[:m] -> 처음부터 (m-1)까지 출력
# print("뒤 7자리 : " + pn[7:]) # ab[n:] -> n번째부터 끝까지 출력

# # 음수 -> 뒤에서부터 자리수 계산 (맨 뒤의 문자 == -1)
# print("뒤 7자리(뒤) : " + pn[-7:]) # 뒤에서부터 7번째~끝까지 출력



# # 문자열 처리 함수
# python = "Python is Amazing"
# print(python.lower())  # 모든 문자 소문자로 출력
# print(python.upper())  # 모든 문자 대문자로 출력
# print(python[4].isupper())  # python의 5번째 값이 대문자인가? -> false
# print(len(python))  # len() : 문자열의 길이

# length = len(python)
# print(length - 7)

# print(python.replace("Python", "Java"))  #ab.replace("n", "m") : n을 m으로 바꾼다
# Java = python.replace("Python", "Java")
# print(Java)

# index = python.index("i") # ab.index("n")  :  변수에서 n 이 몇번째에 위치하는지 출력 
# print(index)
# index2 = python.index("i", index + 1) # ab.index("n", s): s == 문자 추적 시작 위치
# print(index2)

# find = python.find("i") # find : index와 비슷
# print(find)

# print(python.find("Amazing")) # 문자열 추적시 해당 문자열의 첫번째 문자 위치 출력

# print(python.find("Java"))  # 변수에 해당 문자가 없을 시 -1 출력
# # print(python.index("Java")) # 변수에 해당 문자가 없을 시 오류 발생

# count = python.count("i")  # 변수에서 해당 문자의 등장 횟수 출력
# print(count)



# # 문자열 포맷
# print("a" + "b")
# print("a", "b")

# # 방법 1
# print("나는 %d살입니다." % 25) # %d : 정수
# print("나는 %s을/를 좋아합니다." % "배드민턴") # %s : 문자열, 한 문자, 정수 가능
# print("나는 %s살입니다." %25)
# print("Apple은 %c로 시작합니다." %"A")  # %c : 한 글자
# print("나는 %s색과 %s색을 좋아합니다." %("검정", "하늘")) # 순서대로 대입됨

# # 방법 2
# print("나는 {}살입니다.".format(25)) # .format() : 괄호안의 값을 {}에 대입
# print("나는 {}살입니다.".format("스물다섯")) # 문자열도 가능
# print("나는 {}색과 {}색을 좋아합니다.".format("검정", "하늘")) # 순서대로 대입
# print("나는 {2}색과 {0}색을 좋아합니다.".format("검정", "하늘", "연두"))
# # -> {n} n번재에 있는 값 대입

# # 방법 3
# print("나는 {age}살이며, {color}색을 좋아합니다.".format(age = 25, color = "하늘"))
# print("나는 {age}살이며, {color}색을 좋아합니다.".format(color = "하늘", age = 25))
# # 순서가 바뀌어서 상관 x

# # 방법 4
# age = 25
# color = "하늘"
# print(f"나는 {age}살이며, {color}색을 좋아합니다.")
# # f"--{}--" : {}에 미리 선언한 변수를 대입할 수 있음

# animal1 = "강아지"
# animal2 = "고양이"
# str = f"나는 {animal1}와 {animal2}, 모두 좋아합니다."
# print(str)



# # 탈출문자
# # print("백문이 불여일견
# # 백견이 불여일타")    #오류

# print("백문이 불여일견\n백견이 불여일타") # \n : 줄바꿈

# # 저는 "사나이"입니다.
# # print("저는 "사나이"입니다.") # 오류
# print('저는 "사나이"입니다.')
# print("저는 \"사나이\"입니다.") # \" , \' : 문장내에서 ", '를 표현 가능

# # \\ -> 문장내에서 \
# # print("C:\Users\김영기\Desktop\Python Workspace>") # 오류
# print("C:\\Users\\김영기\\Desktop\\Python Workspace>")

# # \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine") # \r뒤의 문자수만큼 첫번째문자부터 덮어씀

# # \b : \의 앞글자 백스패이스 (한글자 삭제)
# print("redd\bapple") # 출력 : redapple
# print("blue \b sky") # 출력 : blue sky

# # \t : 키보드상의 탭과 동일(여러칸 띄어쓰기)
# print("Red\tapple") # Red     apple