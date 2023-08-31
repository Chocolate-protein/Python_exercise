# 텍스트 & 엔트리
# 텍스트 창 : 줄바꿈 가능
# 엔트리 창 : 줄바꿈 불가(한줄만 입력 가능)

from tkinter import *

root = Tk()
root.title("test GUI")    # 제목
root.geometry("640x400")

# 창 내에 텍스트 위젯 만들기
txt = Text(root, width=30, height=5)
txt.pack()

# 선입력
txt.insert(END, "글자를 입력하세요")

# 엔트리 위젯 만들기
e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력하세요")


def btncmd():
    # 내용 출력
    # .get("L.I", END) : L번째 줄의 I번째부터 END까지의 문자를 출력한다
    print(txt.get("1.0", END))  # 1: 첫번째 라인, 0: 0번째 column 위치(인덱스)
    print(e.get())  # 엔트리

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()