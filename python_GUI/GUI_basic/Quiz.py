# Quiz) 메모장 만들기

import os
from tkinter import *

root = Tk()
root.title("제목없음 - Windows 메모장")
root.geometry("640x480")


# 열기, 저장 파일 이름
filename = "mynote.txt"

# 파일 메뉴 함수
def open_file():
    if os.path.isfile(filename):   # 해당 파일이 있는가? -> 있으면 True, 없으면 False
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END)   # 텍스트 위젯 본문 삭제
            txt.insert(END, file.read()) # 파일 내용을 본문에 입력

def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END))   # 모든 내용을 가져와서 저장


# 메뉴
menu_ = Menu(root)

# 파일 메뉴
menu_file = Menu(menu_, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()

menu_file.add_command(label="끝내기", command=root.quit)

menu_.add_cascade(label="파일", menu=menu_file)

# 그외 메뉴(빈 메뉴)
menu_.add_cascade(label="편집")
menu_.add_cascade(label="서식")
menu_.add_cascade(label="보기")
menu_.add_cascade(label="도움말")


# 스크롤바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# 텍스트창
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)

scrollbar.config(command=txt.yview)   # 스크롤바 동기화

root.config(menu=menu_)   # 메뉴 동기화



root.mainloop()