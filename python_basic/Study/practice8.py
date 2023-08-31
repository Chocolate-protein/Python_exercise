# 8-1) 표준 입출력
'''
print("Python", "Java", "JavaScript", sep = " vs ")
# 출력 Python vs Java vs JavaScript
# sep = "": print 함수에서, 자리에 무엇을 출력할지 결정(기본값 : " ")

print("Python", "Java", sep = ", ", end = "? ")
print("무엇이 더 재밌을까요?")
# end = "": 문장의 끝부분에 출력할 내용 결정(기본값 : "\n")
# 출력 : Python, Java? 무엇이 더 재밌을까요?
'''

# import sys
# print("python", "java", file=sys.stdout)  # 표준 출력
# print("python", "java", file=sys.stderr)  # 표준 에러
'''
scores = {"수학":0, "영어":50, "국어":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")
    # ljust(n) : n만큼 공간을 확보하고 왼쪽정렬
    # rjust(n) : n만큼 공간을 확보하고 오른쪽정렬
'''

# 은행 대기순번표 : 001, 002, 003, ... 
'''
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))
    # .zfill(n) : n만큼 공간을 확보하고 문자대입, 빈공간은 0으로 출력
'''
'''
answer = input("값을 입력하세요 : ")
print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")
'''



# 8-2) 다양한 출력포맷
'''
# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))    # 500
print("{0: >10}".format(-500))   # -500

# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))   # +500
print("{0: >+10}".format(-500))  # -500

# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500))

# 3자리 마다 콤마 찍어주기
print("{0:,}".format(100000000000))

# 3자리 마다 콤마 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(100000000000))
print("{0:+,}".format(-100000000000))

# 3자리 마다 콤마를 찍어주기, 부호 붙이기, 자릿수 확보하기
# 빈자리는 ^ 로 채우기
print("{0:^<+30,}".format(100000000000))
# 순서 : 출력할 내용, :, 빈자리 채울 내용, 정렬방향, 부호 여부, 자릿수, 콤마(,)

# 소수점 출력
print("{0:f}".format(5/3))

# 소수점 특정 자리수까지만 출력
print("{0:2f}".format(5/3)) # 소수점 2번째까지만 표시(3번째에서 반올림)
'''



# 8-3) 파일 입출력
'''
score_file = open("score.txt", "w", encoding="utf8") # w : write -> (덮어)쓰기
# score_file 이란 파일을 쓰기목적으로 연다.
print("수학 : 0", file=score_file)   # 해당 내용을 score_file에 쓴다.
print("영어 : 50", file=score_file)  # print 함수는 자동 줄바꿈이 있음.
score_file.close()  # 사용한 파일 닫아야함
'''
'''
# 이미 있는 파일에 내용 추가 -> "a" 형식(append)
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n국어 : 100")  # .write 에는 자동 줄바꿈 x
score_file.close()
'''
'''
# 파일 (한번에)읽어오기
score_file = open("score.txt", "r", encoding="utf8")
# score_file 이른 파일을 읽기 목적으로 연다.
print(score_file.read())
score_file.close()
'''
'''
# 파일 한줄씩 출력하기
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 다음줄로 커서 이동
print(score_file.readline()) # 자동으로 줄바꿈이 1회씩 발생함
print(score_file.readline())
print(score_file.readline())
score_file.close()
'''
'''
# 몇줄인지 모를 경우의 한줄씩 출력
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()
'''
'''
# 리스트를 통해 출력
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")

score_file.close()
'''



# 8-4) pickle
'''
import pickle

profile_file = open("profile.pickle", "wb") # encoding 필요 x
 # wb -> w : 쓰기, b : binary type 정의     
profile = {"이름":"김영기", "나이":"25", "취미":"헬스"}
print(profile)
pickle.dump(profile, profile_file)  # .dump(적을 내용, 사용할 파일)
# profile 에 있는 정보를 prifile_file 에 저장
profile_file.close()


# file에서 데이터 가져오기
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
 # profile_file 에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()
'''



# 8-5) with

# import pickle
'''
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))  # close 필요 x
'''

# with 를 이용하여 파일 쓰기
'''
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("hello, world")
'''

'''
with open("study.txt", "a", encoding="utf8") as study_file:
    study_file.write("\numm...")
'''

# 파일 불러오기
'''
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
'''