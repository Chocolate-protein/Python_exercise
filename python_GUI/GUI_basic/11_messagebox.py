# 메시지 박스

import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("test GUI")    # 제목
root.geometry("640x480")   # 가로 * 세로 (창 크기), 좌표(창 위치)

# ex : 기차 예매 시스템
def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")
    # .showinfo("창 제목", "메시지 내용")

def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.")
    # .showwarnning("창 제목", "메시지 내용")

def error():
    msgbox.showerror("에러", "잔액이 부족합니다.")

def okcancel():
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?")

def retrycancel():
    response = msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")
    if response == 1:  # 재시도
        print("재시도")
    elif response == 0:  # 취소
        print("취소")
    
def yesno():
    msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향 입니다. 예매하시겠습니까?")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다. \n 저장 후 프로그램을 종료하시겠습니까?")
    # 네 : 저장 후 종료
    # 아니오 : 저장 하지 않고 종료
    # 취소 : 프로그램 종료 취소
    print("응답 : ", response)   # True / False / None -> 1 / 0 / 그 외
    if response == 1:  # 예
        print("예")
    elif response == 0:  # 아니오
        print("아니오")
    else:
        print("취소")

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()

Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()

root.mainloop()