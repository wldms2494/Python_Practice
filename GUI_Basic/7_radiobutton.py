# 라디오 버튼은 여러개중 택 1 하는것 

from tkinter import * # 티킨터
root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 x 세로

label1 = Label(root, text = "메뉴를 선택하세요").pack()

burger_var = IntVar() # 여기에 int형으로 값을 저장
btn_burger1 = Radiobutton(root,text="햄버거", value=1, variable=burger_var)
btn_burger1.select() # 디폴트값은 햄버거
btn_burger2 = Radiobutton(root,text="치즈버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root,text="치킨버거", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

label2 = Label(root, text = "메뉴를 선택하세요").pack()

drink_var = StringVar() # value 가 한글이기에 StringVar()로 설정
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print('선택된 value : ',burger_var.get())
    print('선택된 value : ',drink_var.get())
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()