# 5635번) 생일

n = int(input())
data = list()

for i in range(0, n):
    data.append(input().split())

data.sort(key = lambda x: (int(x[3]), int(x[2]), int(x[1])))

print(data[len(data)-1][0])
print(data[0][0])


'''
n = int(input())

year_min = 1990
year_max = 2010
month_min = 1
month_max = 12
day_min = 1
day_max = 31

for _ in range(0, n):
    name, d, m, y = map(str, input().split())
    if int(y) > year_min:
        year_min = int(y)
        month_min = int(m)
        day_min = int(d)
        person_min = name
    elif int(y) == year_min:
        year_min = int(y)
        if int(m) > month_min:
            month_min = int(m)
            day_min = int(d)
            person_min = name
        elif int(m) == month_min:
            month_min = int(m)
            if int(d) > day_min:
                day_min = int(d)
                person_min = name
    if int(y) < year_max:
        year_max = int(y)
        month_max = int(m)
        day_max = int(d)
        person_max = name
    elif int(y) == year_max:
        year_max = int(y)
        if int(m) < month_max:
            month_max = int(m)
            day_max = int(d)
            person_max = name
        elif int(m) == month_max:
            month_max = int(m)
            if int(d) < day_max:
                day_max = int(d)
                person_max = name

print(person_min)
print(person_max)
'''