# 6-1) if
'''
if 조건:        #  ":" 으로 조건 문장 마무리
    실행 명령문
'''

# weather = input("오늘 날씨는 어때요? : ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#      print("준비물은 필요 없습니다")

# temp = int(input("기온은 어때요?"))
# if 30 <= temp:
#     print("너무 덥습니다. 외출을 자제하세요")
# elif 10 <= temp and 30 > temp:
#     print("날씨가 좋습니다.")
# elif 0 <= temp < 10:
#     print("날씨가 춥습니다. 외투를 챙기세요")
# else:
#     print("너무 춥습니다. 외출을 자제하세요")



# 6-2) 반복문 : for
# print("대기번호 : 1")
# print("대기번호 : 2") ...

'''
for 변수 in 리스트(또는 튜플, 문자열):
    수행할 문장1
    수행할 문장2
    ...
'''

# for waiting_no in range(1, 5):  
#     print("대기번호 : {0}".format(waiting_no))

# cafe = ["유재석", "김종국", "송지효"]
# for customer in cafe:
#     print("{0}님, 주문 도와드리겠습니다.".format(customer))

'''
a = ...
for b = in a:
    print("{0}".format(b))
'''



# 6-3) 반복문 : while

'''
while <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    <수행할 문장3>
'''

# customer = "김종국"
# index = 4
# while index >= 0:
#     print("{0} 님, 음료가 준비 되었습니다. {1} 번 남았습니다".format(customer, index))
#     index -= 1
#     if index == -1:
#         print("음료는 폐기처분되었습니다.")

# # 무한루프
# customer = "유재석"
# i = 1
# while True:
#     print("{0} 님, 음료가 준비되었습니다. 호출 {1}회".format(customer, i))
#     i += 1


# customer = "송지효"
# person = "Unkown"

# while person != customer :
#     print("{0} 님, 음료가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")
#     if person == customer:
#         print("음료 여기 있습니다. 맛있게 드세요")



# # 6-4) continue, break
# absent = [2, 5]  # 결석
# no_book = [7] # 책 놓고옴
# for student in range(1, 11): # 1~10 출석번호
#     if student in absent:
#         continue    # 문장을 실행하지 않고 다음 문장으로 넘어감
#     elif student in no_book:
#         print("오늘은 여기까지, {0}번은 진실의 방으로".format(student))
#         break       # 문장을 실행하지 않고 반복문 탈출
#     print("{0}번".format(student))


# # 6-5) 한 줄 for
# # ex)출석번호 1 2 3 4 5, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104, 105
# student = range(1, 5+1)
# student = list(student)
# print(student)
# student = [i+100 for i in student] # student에 있는 i값에 100을 더한 후 리스트에 삽입
# print(student)  # 출력 : [101, 102, 103, 104, 105]

# # 학생 이름을 길이로 변환
# student = ["Kim", "Park", "Song"]
# student = [len(i) for i in student] # student에 있는 i값을 길이로 변환 후 리스트에 삽입
# print(student)  # 출력 : [3, 4, 4]

# # 학생 이름 대문자로 변환
# student = ["Kim", "Park", "Song"]
# student = [i.upper() for i in student]
# print(student) # 출력 : [KIM, PARK, SONG]