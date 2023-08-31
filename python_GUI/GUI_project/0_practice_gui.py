# lst = list(range(1, 6))
# lst.reverse()
# print(lst)

# lst2 = list(range(1, 6))
# print("리스트 2 뒤집기 전 : ", lst2)

# lst3 = reversed(lst2)
# print("리스트 2 뒤집은 후 : ", lst2)
# print("리스트 3 : ", list(lst3))

# # list.reverse() : 원본값 자체를 뒤집는다
# # reversed(list) : 뒤집힌 원본값을 반환하고, 원본 자체는 변하지 않는다.


kor = ["사과", "바나나", "오렌지"]
eng = ["apple", "banana", "orange"]

print(list(zip(kor, eng)))   # zip(list1, list2)세로로 합침

mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]
print(list(zip(*mixed)))   # zip(*list)각 그룹별 같은 인덱스끼리 분리

kor2, eng2 = zip(*mixed)
print(kor2)
print(eng2)