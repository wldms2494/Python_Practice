from tkinter import * # 티킨터
root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 x 세로

txt = Text(root, width=30, height=5) 
txt.pack() # 텍스트 박스 완성
txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30) # 한줄로 입력 받음. 엔터를 입력할 수 없음
e.pack()
e.insert(0, "한줄만 입력해요")

def btncmd():
    print(txt.get("1.0",END)) # 1.0 -> 1은 라인 1부터 가져와라. 0은 0번째 컬럼 위치
    print(e.get())

    txt.delete("1.0", END)
    e.delete(0, END) # 클릭 후 내용 출력 및 삭제
btn = Button(root, text="클릭", command=btncmd)
btn.pack()
root.mainloop()