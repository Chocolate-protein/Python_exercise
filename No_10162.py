# 10162번) 전자레인지

from math import *

count_a = 0
count_b = 0
count_c = 0

time = int(input())

if time < 60:
    count_c = time//10

elif 60 <= time < 300:
    count_b = floor(time/60)
    count_c = (time%60)//10

elif time >= 300:
    count_a = floor(time/300)
    if time%300 >= 60:
        count_b = floor((time%300)/60)
        count_c = ((time%300)%60)//10
    else:
        count_c = (time%300)//10

if time%10 != 0:
    print(-1)
else:
    print("{} {} {}".format(count_a, count_b, count_c))