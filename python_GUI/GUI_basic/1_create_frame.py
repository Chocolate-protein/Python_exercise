# 프레임

from tkinter import *

root = Tk()
root.title("test GUI")    # 제목
root.geometry("640x480")   # 가로 * 세로 (창 크기), 좌표(창 위치)
# .geometry("가로 x 세로 + x좌표 + y좌표")

root.resizable(False, False)   # x(너비), y(높이) 값 변경 불가(창 크기 고정)

root.mainloop()