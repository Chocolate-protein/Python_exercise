# 2750번) 수 정렬하기

n = int(input())
n_list = list()

for _ in range(0, n):
    n_list.append(int(input()))

n_list.sort()

for i in n_list:
    print(i)

# 오름차순 : list.sort() == list.sort(reverse = )
# 내림차순 : list.sort(reverse = True)