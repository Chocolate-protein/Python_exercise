# 스크롤 바

from tkinter import *

root = Tk()
root.title("test GUI")    # 제목
root.geometry("640x480")   # 가로 * 세로 (창 크기), 좌표(창 위치)

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="both")

# set이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
for i in range(1, 32):
    listbox.insert(END, str(i) + "일")
listbox.pack(side="left")

# 리스트박스와 스크롤바 맵핑(연결, 동기화)
scrollbar.config(command=listbox.yview)

root.mainloop()