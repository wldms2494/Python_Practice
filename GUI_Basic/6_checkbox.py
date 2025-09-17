from tkinter import * # 티킨터
root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 x 세로

chkvar = IntVar() # chkvar 에 int 형으로 값을 저장한다. 
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar) # variable은 체크박스의 값이 들어가는 변수 
# chkbox.select() # 자동 선택처리 
# chkbox.deselect() # 선택 해제 처리 
chkbox.pack()
chkvar2 = IntVar() # chkvar 에 int 형으로 값을 저장한다. 
chkbox2 = Checkbutton(root, text="일주일 동안 보지 않기", variable=chkvar2 )
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0일때는 체크 해제, 1일때 체크
    print(chkvar2.get())
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()