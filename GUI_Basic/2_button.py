from tkinter import * # 티킨터
root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 x 세로
#root.geometry("640x480+100+100") # 가로 x 세로 + x좌표 + y좌표
#root.resizable(False, False)  # x(너비), y(너비) 값 변경 변경 불가 (창 크기 변경 불가)

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼222222222")  #버튼이 자동으로 커짐
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4") # 글자가 길어도 짤리지 고정된 크기라 버튼 크기는 변하지 않음
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5") 
btn5.pack()

photo = PhotoImage(file="GUI_Basic/image.png")
btn6 = Button(root, image=photo) 
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")
btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()
root.mainloop()