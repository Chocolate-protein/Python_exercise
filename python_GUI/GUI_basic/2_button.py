# 버튼 

from tkinter import *

root = Tk()
root.title("test GUI")    # 제목

btn1 = Button(root, text="버튼1")
btn1.pack()   # 버튼을 화면에 표출

 # padx/y : 추가 여백 -> 문자 많으면 버튼 크기 커짐
btn2 = Button(root, padx=5, pady=10, text="버튼2222222222")  
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

# width/height : 고정된 크기 -> 문자 많으면 문자가 잘림
btn4 = Button(root, width=10, height=3, text="버튼44444")   
btn4.pack()

# fg : 글자 색, bg = 배경 색
btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

# 이미지파일로 버튼 생성
photo = PhotoImage(file="C:\\Users\\김영기\\Desktop\\Python Workspace\\python_GUI\\images\\button.png")
btn6 = Button(root, image=photo)
btn6.pack()

# 버튼 동작 설정
def btncmd():
    print("버튼이 클릭되었습니다")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()


root.mainloop()