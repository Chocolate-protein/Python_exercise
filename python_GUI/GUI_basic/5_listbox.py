# 리스트 박스 : 여러줄에 걸쳐 목록 관리하는 위젯

from tkinter import *

root = Tk()
root.title("test GUI")    # 제목
root.geometry("640x400")

listbox = Listbox(root, selectmode="extended", height=0)
# selectmode= extended : 여러개 동시 선택 가능, single : 하나씩만 선택 가능
# height = 0 : 내용만큼 자동으로 창크기 설정, n : n만큼 창크기 설정(스크롤 가능)

listbox.insert(0, "사과")   # .insert(추가할 위치(인덱스), 내용)
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")   # END -> 가장 뒷부분에 추가
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    # 삭제
    # listbox.delete(END)  # .delete(n) : n번째 항목 삭제

    # 갯수 확인
    # print("리스트에는", listbox.size(), "개가 있습니다.")

    # 항목 확인
    # print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))

    # 선택한 항목 확인 : 인덱스값(위치)으로 반환(1, 2, 3)
    print("선택된 항목 : ", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()