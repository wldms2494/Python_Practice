# you can't get over the fact that people who are not white are better than you
# Quiz) tkinter를 이용한 메모장 프로그램을 만드세요

# GUI 조건
# 1. title: "제목 없음" - windows 메모장
# 2. 메뉴 : 파일, 편집, 서식, 보기, 도움말
# 3. 실제 메뉴 구현 : 파일 메뉴 내에서 열기, 저장, 끝내기 3개만 처리
# 3-1. 열기 : mynote.txt. 파일 내용 열어서 보여주기
# 3-2. 저장 : mynote.txt. 파일에 현재 내용 저장하기
# 3-3. 끝내기 : 프로그램 종료
# 4. 프로그램 시작 시 본문은 비어있는 상태
# 5. 하단 ㄴtatus 바는 필요 없음
# 6. 프로그램 크기, 위치는 자유롭게 하되 크기 조정 가능해야 함.
# 7. 본문 우측 상하 스크롤바 넣기
import os
from tkinter import *
root= Tk()
root.title("제목 없음 - windows 메모장")
root.geometry("640x480")

# 열기 저장 파일 이름
filename = "mynote.txt"

# 열기, 저장, 닫기 메소드
def open_file():
    if os.path.isfile(filename): #파일이 있으면 True, 없으면 False
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END) # 기존의 창에 얹여지기 때문에 내용을 삭제하고 표시
            txt.insert(END, file.read())  #화면에 표시
def save_file():
    with open(filename, "w", encoding="utf-8") as file:
        file.write(txt.get("1.0", END)) # 모든 내용을 가져와서 저장
# 메뉴만들기
menu = Menu(root)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command = open_file)
menu_file.add_command(label="저장", command = save_file)
menu_file.add_separator()
menu_file.add_command(label="닫기", command = root.quit)
menu_edit = Menu(menu, tearoff=0)
menu_selection = Menu(menu, tearoff=0)
menu_view = Menu(menu, tearoff=0)
menu_help = Menu(menu, tearoff=0)


# 메뉴 실제로 추가하기
menu.add_cascade(label="파일", menu = menu_file)
menu.add_cascade(label="편집", menu = menu_edit)
menu.add_cascade(label="서식", menu = menu_selection)
menu.add_cascade(label="보기", menu = menu_view)
menu.add_cascade(label="도움말", menu = menu_help)
root.config(menu = menu)


# 스크롤바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# 본문영역 그리기
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True) # root를 꽉채우기 
scrollbar.config(command=txt.yview)
root.mainloop()