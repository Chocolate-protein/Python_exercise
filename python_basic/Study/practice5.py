# # 5-1) 리스트 []
# # : 지하철 칸별 10, 20, 30명
# # subway1 = 10
# # subway2 = 20
# # subway3 = 30

# # subway = [10, 20, 30]
# # print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# # 조세호가 몇 번째 칸에 타고 있는가
# print(subway.index("조세호"))

# # 다음 정류장에서 하하가 탔음
# subway.append("하하")   # .append() : 리스트 맨 뒤에 추가
# print(subway)

# # 정현돈을 유재석가 조세호 사이에 태움
# subway.insert(1, "정형돈") # .insert(n, "m") : "m"을 n번 위치에 추가
# print(subway)

# # 지하철에 있는 사람을 한명씩 뒤에서 꺼냄
# subway.pop()
# print(subway)    # .pop(n) : 리스트에서 n번째에 있는 것 삭제

# # subway.pop()     # n생략이 맨 뒤 부터 자동 삭제 
# # print(subway)

# # subway.pop(0)
# # print(subway)

# # 같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")  # 유재석 맨 뒤에 추가
# print(subway)
# print(subway.count("유재석"))

# # 정렬
# num_list = [5, 3, 4, 1, 2]
# print(num_list)
# num_list.sort()  # .sort() : 순서대로 정렬
# print(num_list)

# # # 순서 뒤집기
# # num_list.reverse()
# # print(num_list)

# # 선택하여 지우기
# num_list.remove(5)
# print(num_list)

# # 모두 지우기
# num_list.clear()  # .clear : 리스트 모두 삭제
# print(num_list)

# # 다양한 자료형 함께 사용 가능
# mix_list = ["샤인머스캣", 20, True]
# print(mix_list)
# # mix_list.sort()  # 오류 : 다른 자료형일 경우 정렬 안됨

# # 리스트 확장
# num_list = [5, 3, 4, 1, 2]
# num_list.extend(mix_list)  # 리스트1.extend(리스트2) : 리스트2를 1뒤에 추가
# print(num_list)

# ex1 = ["가", "다", "나"]
# ex1.sort()   # print(ex.sort()) 할 시 None 출력, print 함수에 바로 넣지 말 것
# print(ex1)   # 출력 : ['가', '나', '다']

# ex2 = [True, False, True]
# ex2.sort()
# print(ex2)   # 출력 : [False True True]



# # 5-2) 사전 : 선언 {} / 사용 []
#  # 3번 key를 "유재석", 100번 key를 "김태호"가 받았음
# cabinet = {3:"유재석", 100:"김태호"} 
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# # print(cabinet[5])  # 5 key를 배정안했기 때문에 오류 및 종료
# print(cabinet.get(5)) # .get() 사용시 배정안된 key 입력하면 None 출력 후 다음문장 실행
# print("hi")
# print(cabinet.get(5, "박명수"))  # 5번 key에 임시로 박명수 배정
# # print(cabinet[5])  # 오류 : 윗 문장에서 임시로 배정했기 때문에 다시 비어있음

# # key 배정 여부 확인 : prin(key_num in 변수)
# print(3 in cabinet)  # True
# print(5 in cabinet)  # False

# # 정수가 아닌 str 자료형도 가능
# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet.get("B-100"))

# # 새로운 key 할당 : []   ( 처음 선언, 할당 : {} )
# print(cabinet)
# cabinet["C-20"] = "조세호" 
# cabinet["A-3"] = "김종국"   # 중복 key 선언시 덮어쓰기
# print(cabinet)

# # key 삭제
# del cabinet["B-100"]
# print(cabinet)

# # 현재 할당중인 key 들만 출력
# print(cabinet.keys())

# # 현재 할당중인 value 들만 출력
# print(cabinet.values())

# # 현재 할당중인 key, value 함께 출력
# print(cabinet.items())

# # 모든 key에 배정된 value들 삭제
# cabinet.clear()
# print(cabinet)



# # 5-3) 튜플(내용 변경, 추가 X, but 속도 빠름)

# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# menu.add("생선까스") # 오류 : 변경, 추가 안됨

# name = "김종국"
# age = 20
# hobby = "운동"
# print(name, age, hobby)

# name, age, hobby = "김종국", 20, "운동"  # 튜플식
# print(name, age, hobby)



# # 5-4) 세트(set) : 중복 X, 출력 순서 랜덤
# my_set = {1, 2, 3, 3, 3}
# print(my_set) # 출력 : {1, 2, 3} -> 중복 안됨

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# # 교집합 (java, python 모두 포함인 사람)
# print(java & python)
# print(java.intersection(python))  # 출력 : {'유재석'}

# # 합집합 (java or python 가능한 사람)
# print(java | python)         # 유재석 김태호 양세형 박명수 모두 출력
# print(java.union(python))   

# # 차집합(java 가능, but python 못하는 사람)
# print(java - python)  # 양세형 김태호 출력
# print(java.difference(python))

# # python 인원 늘어남
# python.add("김태호")
# print(python)

# # java 인원 감소함
# java.remove("김태호")
# # java.remove(1)  # 오류 : 순서가 없기 때문에 번호로 지정 x
# print(java)



# # 5-5) 자료구조 변경

# # cafe
# menu = {"coffee", "milk", "juice"}
# print(menu, type(menu))   # type() : 해당 변수의 type 출력
# # 출력 : {'milk', 'coffee', 'juice'} <class 'set'>

# menu = list(menu)    # 변수 menu의 type을 list로 변경
# print(menu, type(menu))
# # 출력 : ['milk', 'coffee', 'juice'] <class 'list'>
# # {} : set type ,  [] : list type

# menu = tuple(menu)  # 변수의 type을 tuple로 변경
# print(menu, type(menu))
# # 출력 : ('milk', 'coffee', 'juice') <class 'tuple'>
# # () : tuple type

# menu = set(menu)
# print(menu, type(menu))