# 레이블

from tkinter import *

root = Tk()
root.title("test GUI")    # 제목
root.geometry("640x400")

label1 = Label(root, text="hi")
label1.pack()

photo = PhotoImage(file="C:\\Users\\김영기\\Desktop\\Python Workspace\\python_GUI\\images\\button.png")
label2 = Label(root, image=photo)
label2.pack()


def change():
    label1.config(text="see you later")
    
    global photo2   # 전역변수로 선언해야 이미지가 삭제되지 않음
    photo2 = PhotoImage(file="C:\\Users\\김영기\\Desktop\\Python Workspace\\python_GUI\\images\\change.png")
    label2.config(image=photo2)

btn = Button(root, text="click", command=change)
btn.pack()

root.mainloop()