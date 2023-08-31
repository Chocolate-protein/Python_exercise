# 4673번) 셀프 넘버

natural_num = list(range(1, 10001))
notself_num = list()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    notself_num.append(i)
    set(notself_num)

self_num = list(set(natural_num).difference(notself_num))
self_num.sort()
for k in self_num:
    print(k)