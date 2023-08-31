# # 7-1) 함수
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# open_account()


# # 7-2) 전달값과 반환값
# def deposit(balance, money):   # 입금함수
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance+money))
#     return balance + money

# def withdraw(balance, money):  # 출금함수
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance-money))
#         return balance - money
#     else:
#         print("잔액이 부족합니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money):  # 저녁에 출금 -> 수수료 100원
#     commission = 100 # 수수료 100원
#     print("출금이 완료되었습니다. 수수료는 {0}원이며, 잔액은 {1} 원입니다.".format(commission, balance - money - commission))
#     return commission, balance - money - commission
    

# balance = 0  # 잔액
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료는 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))


# *줄바꿈 : \ 입력후 뒷부분 enter
# ex) print("안녕하세요. \
# 반갑습니다.")


# # 7-3) 기본값

# def profile(name, age, main_lang):
#     print("이름은 : {0} \t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

# profile("유재석", 40, "python")
# profile("김영기", 25, "C++")

# # ex 같은 학교, 같은 학년, 같은 반, 같은 수업.
# def profile(name, age=17, main_lang="python"):
#     print("이름은 : {0} \t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

# profile("김영기")



# # 7-4) 키워드값
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name = "김영기", main_lang="C++", age = 25)



# # 7-5) 가변인자
# # end=" " : 출력 문장이 끝나도 줄을 바꾸지 않고 다음문장을 이어서 출력

# # def profile(name, age, lang1, lang2, lang3, lang4, lang5):
# #     print("이름 : {0} \t나이 : {1} \t".format(name, age), end="")
# #     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("유재석", 43, "python", "C", "java", "C#", "C++", "java")
# profile("김영기", 25, "python", "C", "C++", "", "")



# 7-6) 지역변수와 전역변수
# ex) 군대
gun = 10   # 전역 변수

def checkpoint(soldiers):  # 지역변수 soldiers 선언
    # gun = 20   : 지역변수
    global gun  # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {}".format(gun))

def checkpoint_return(gun, soldiers):  # 지역변수 gun, soldiers 선언
    gun = gun - soldiers   # 지역변수
    print("[함수 내] 남은 총 : {}".format(gun))
    return gun   # 지역변수 gun 전역공간으로 반환 -> 전역변수 gun 갱신

print("전체 총 : {0}".format(gun))
# checkpoint(2)  # 2명 경계근무
gun = checkpoint_return(gun, 2)

print("남은 총 : {}".format(gun))