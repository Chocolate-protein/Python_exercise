# 라디오 버튼 : 여러개 버튼중 하나만 선택 가능(다른 버튼 자동 해제)

from tkinter import *

root = Tk()
root.title("test GUI")    # 제목
root.geometry("640x480")   # 가로 * 세로 (창 크기), 좌표(창 위치)

Label(root, text="메뉴를 선택하세요").pack()

# 체크 박스와 달리 하나의 바를 공유
burger_var = IntVar()
btn_burger1 = Radiobutton(root, text="싸이버거", value=1, variable=burger_var)
btn_burger2 = Radiobutton(root, text="화이트갈릭버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="에멘탈치즈버거", value=3, variable=burger_var)
btn_burger3.select()   # 버튼 자동 선택

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="음료를 선택하세요").pack()

drink_var = StringVar()   # value 가 문자열이기 때문에 StringVar 설정
btn_drink1 = Radiobutton(root, text="코카콜라", value="코카콜라", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="펩시", value="펩시", variable=drink_var)
btn_drink3 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()

def btncmd():
    print(burger_var.get())   # 햅버거 중 선택된 라디오 항목의 값(value)
    print(drink_var.get())   # 음료중 선택된 value 출력

btn = Button(root, text="Order", command=btncmd)
btn.pack()

root.mainloop()