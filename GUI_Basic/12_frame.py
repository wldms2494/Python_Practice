# Message box : 에러가 발생했을때 뜨는 팝업
import tkinter.messagebox as msgbox
from tkinter import * # 티킨터
root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 x 세로

Label(root, text="메뉴를 선택해주세요").pack(side="top")
Button(root, text="주문하기").pack(side="bottom")
frame_burger = Frame(root, relief="solid", bd=1) # relief : 테두리
frame_burger.pack(side="left",fill = "both", expand=True)
Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right",fill = "both", expand=True)
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()
root.mainloop()