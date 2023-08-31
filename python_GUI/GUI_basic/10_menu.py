# 메뉴 바

from tkinter import *

root = Tk()
root.title("test GUI")    # 제목
root.geometry("640x480")   # 가로 * 세로 (창 크기), 좌표(창 위치)

def create_new_file():
    print("새 파일을 만듭니다.")

menu_ = Menu(root)

# File 메뉴
menu_file = Menu(menu_, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")

menu_file.add_separator()   # 구분자
menu_file.add_command(label="Open File...")

menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable")   # 비활성화

menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)

menu_.add_cascade(label="File", menu=menu_file)   # 메뉴 창 추가

# Edit 메뉴(빈 값)
menu_edit = Menu(menu_, tearoff=0)
# menu_edit.add_command(label="Undo        Ctrl+Z")
menu_.add_cascade(label="Edit", menu=menu_edit)

# language 메뉴 추가 : radio 버튼을 통해 택 1
menu_lang = Menu(menu_, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu_.add_cascade(label="Language", menu=menu_lang)

# View 메뉴 : 체크버튼 -> 복수 선택 가능
menu_view = Menu(menu_, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu_view.add_checkbutton(label="Show Breadcrumbs")
menu_.add_cascade(label="View", menu=menu_view)


root.config(menu=menu_)
root.mainloop()
