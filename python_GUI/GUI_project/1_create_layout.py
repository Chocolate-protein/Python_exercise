# 레이아웃

import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GUI Image Make")    # 제목

# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x")

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일 추가")
btn_add_file.pack(side="left", padx=3, pady=3)

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="선택 삭제")
btn_del_file.pack(side="right", padx=3, pady=3)


# 리스트 프레임 : 리스트 박스, 스크롤 바
list_frame = Frame(root)
list_frame.pack(fill="both", padx=3, pady=3)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)


# 저장경로 프레임
path_frame = LabelFrame(root, text="저장경로", padx=3, pady=3)
path_frame.pack(fill="x", padx=3, pady=3)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=3, pady=3, ipady=4)   # 높이 변경

btn_dest_path = Button(path_frame, text="찾아보기", padx=3, pady=3, width=10)
btn_dest_path.pack(side="right")


# 옵션 프레임
option_frame = LabelFrame(root, text="옵션", pady=3, padx=5)
option_frame.pack(padx=3, pady=3)

# 1) 가로 넓이 옵션
# 가로넓이 레이블
lbl_width = Label(option_frame, text="가로넓이", width=8)
lbl_width.pack(side="left", padx=3, pady=3)

# 가로넓이 콤보
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(option_frame, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=3, pady=3)

# 2) 간격 옵션
# 간격 옵션 레이블
lbl_space = Label(option_frame, text="간격", width=8)
lbl_space.pack(side="left", padx=3, pady=3)

# 간격 옵션 콤보
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(option_frame, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=3, pady=3)

# 3) 파일 포맷 옵션
# 파일 포맷 레이블
lbl_format = Label(option_frame, text="포맷", width=8)
lbl_format.pack(side="left")

# 파일 포맷 콤보
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(option_frame, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=3, pady=3)

# 진행 상황 Progress Bar
progress_frame = LabelFrame(root, text="진행상황")
progress_frame.pack(fill="x", padx=3, pady=3)

p_var = DoubleVar()
progerss_bar = ttk.Progressbar(progress_frame, maximum=100, variable=p_var)
progerss_bar.pack(fill="x", padx=3, pady=3)

# 실행 프레임
run_frame = Frame(root)
run_frame.pack(fill="both")

btn_close = Button(run_frame, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=3, pady=3)

btn_start = Button(run_frame, padx=5, pady=5, text="시작", width=12)
btn_start.pack(side="right", padx=3, pady=3)


root.resizable(False, False)   # 창 크기 고정
root.mainloop()
