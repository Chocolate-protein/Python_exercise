from datetime import *

today = datetime.today()
print(today.strftime("%Y-%M-%d"))

# .strftime(---) 형식
# %A : 요일,    %B : 해당 월의 실제 이름(EX : MAY)
# %Y : 년도,    %m : 월,    %d : 일
# %H : 시,   %M : 분,    %S : 초