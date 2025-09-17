from tkinter import * # 티킨터

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 x 세로

# pack 복습
# btn1 =Button(root, text="버튼1")
# btn2= Button(root, text="버튼2")

# btn1.pack(side="left") 
# btn2.pack()

# grid는 지정된 좌표에 집어넣음 , pack은 side="left". "right"등을 통해 위치를 조정
# btn1.grid(row=0, column=0)
# btn1.grid(row=1, column=1)


########## Grid 로 계산기 만들기

btn_f16 = Button(root, text="F16", width=5, height=2) # padx, pady 버튼을 x, y축으로 늘려줌
btn_f17 = Button(root, text="F17", width=5, height=2)
btn_f18 = Button(root, text="F18", width=5, height=2)
btn_f19 = Button(root, text="F19", width=5, height=2)

btn_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3) # N, E, W, S => 동서남북 방향
btn_f17.grid(row=0, column=1, sticky=N+E+W+S , padx=3, pady=3)
btn_f18.grid(row=0, column=2, sticky=N+E+W+S , padx=3, pady=3)
btn_f19.grid(row=0, column=3, sticky=N+E+W+S , padx=3, pady=3)

btn_clear = Button(root, text="clear", width=5, height=2)
btn_equal = Button(root, text="=", width=5, height=2)
btn_div = Button(root, text="/", width=5, height=2)
btn_mul = Button(root, text="*", width=5, height=2)

btn_clear.grid(row=1, column=0, sticky=N+E+W+S , padx=3, pady=3)
btn_equal.grid(row=1, column=1, sticky=N+E+W+S , padx=3, pady=3)
btn_div.grid(row=1, column=2, sticky=N+E+W+S , padx=3, pady=3)
btn_mul.grid(row=1, column=3, sticky=N+E+W+S , padx=3, pady=3)

btn_7 = Button(root, text="7", width=5, height=2)
btn_8 = Button(root, text="8", width=5, height=2)
btn_9 = Button(root, text="9", width=5, height=2)
btn_sub = Button(root, text="-", width=5, height=2)

btn_7.grid(row=2, column=0, sticky=N+E+W+S , padx=3, pady=3)
btn_8.grid(row=2, column=1, sticky=N+E+W+S , padx=3, pady=3)
btn_9.grid(row=2, column=2, sticky=N+E+W+S , padx=3, pady=3)
btn_sub.grid(row=2, column=3, sticky=N+E+W+S , padx=3, pady=3)

btn_4 = Button(root, text="4", width=5, height=2)
btn_5 = Button(root, text="5", width=5, height=2)
btn_6 = Button(root, text="6", width=5, height=2)
btn_add = Button(root, text="+", width=5, height=2)

btn_4.grid(row=3, column=0, sticky=N+E+W+S , padx=3, pady=3)
btn_5.grid(row=3, column=1, sticky=N+E+W+S , padx=3, pady=3)
btn_6.grid(row=3, column=2, sticky=N+E+W+S , padx=3, pady=3)
btn_add.grid(row=3, column=3, sticky=N+E+W+S , padx=3, pady=3)

btn_1 = Button(root, text="1", width=5, height=2)
btn_2 = Button(root, text="2", width=5, height=2)
btn_3 = Button(root, text="3", width=5, height=2)
btn_enter = Button(root, text="Enter", width=5, height=2)  #세로로 합쳐짐

btn_1.grid(row=4, column=0, sticky=N+E+W+S , padx=3, pady=3)
btn_2.grid(row=4, column=1, sticky=N+E+W+S , padx=3, pady=3)
btn_3.grid(row=4, column=2, sticky=N+E+W+S , padx=3, pady=3)
btn_enter.grid(row=4, column=3, rowspan=2, sticky=N+E+W+S , padx=3, pady=3) # 현재 위치로부터 아래쪽으로 row를 더함

btn_0 = Button(root, text="0", width=5, height=2)
btn_point= Button(root, text=".", width=5, height=2)

btn_0.grid(row=5,column=0, columnspan=2, sticky=N+E+W+S)
btn_point.grid(row=5, column=2, sticky=N+E+W+S)


root.mainloop()