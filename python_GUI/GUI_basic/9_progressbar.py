# 프로그레스 바 : 퍼센테이지 바(ex: 다운로드, 로딩, ...)

import time
from tkinter import ttk
from tkinter import *

root = Tk()
root.title("test GUI")    # 제목
root.geometry("640x480")   # 가로 * 세로 (창 크기), 좌표(창 위치)

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")  # 바 크기 고정 -> 이동
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")   # 바가 차오름
# progressbar.start(10)   # 10ms 마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop()   # 작동 중지

# btn = Button(root, text="Stop", command=btncmd)
# btn.pack()


p_var2 = DoubleVar()   # 실수형
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01)    # 0.01초 대기

        p_var2.set(i)   # progress bar의 값 설정
        progressbar2.update()   # UI 업데이트
        print(p_var2.get(), "%")


btn = Button(root, text="Start", command=btncmd2)
btn.pack()


root.mainloop()