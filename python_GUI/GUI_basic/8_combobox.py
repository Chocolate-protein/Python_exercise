# 콤보 박스

from tkinter import ttk
from tkinter import *

root = Tk()
root.title("test GUI")    # 제목
root.geometry("640x480")   # 가로 * 세로 (창 크기), 좌표(창 위치)

values1 = [str(i) + "월" for i in range(1, 13)]   # 1 ~ 12 까지의 숫자
month = ttk.Combobox(root, height=5, values=values1)  # 값 변경 가능
month.pack()
month.set("월")   # 최초 목록 제목 설정

values2 = [str(i) + "일" for i in range(1, 32)]   # 1 ~ 12 까지의 숫자
day = ttk.Combobox(root, height=10, values=values2, state="readonly") # 선택만 가능
day.current(0)   # 0번째 인덱스값 자동 선택(기본값)
day.pack()

def btncmd():
    print(month.get(), end=" ")   # 선택된 value 표시
    print(day.get())

btn = Button(root, text="Select", command=btncmd)
btn.pack()

root.mainloop()