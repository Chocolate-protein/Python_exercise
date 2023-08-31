# 체크 버튼

from tkinter import *

root = Tk()
root.title("test GUI")    # 제목
root.geometry("640x480")   # 가로 * 세로 (창 크기), 좌표(창 위치)

chkvar = IntVar()   # chkvar에 int형으로 값을 저장한다
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# chkbox.select()   # 기본값 : 자동 선택 처리
# chkbox.deselect()   # 선택 해제 처리
chkbox.pack()

chkvar2 = IntVar()   # 각각 체크 박스마다 체크바 지정(선언) 필요
chkbox2 = Checkbutton(root, text="일주일 동안 보지 않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get())   # 0 : 체크 해제, 1 : 체크
    print(chkvar2.get())

btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()