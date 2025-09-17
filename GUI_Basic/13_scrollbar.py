from tkinter import * # 티킨터

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 x 세로

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# set이 없으면 스크롤은 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
for i in range(1,32): 
    listbox.insert(END, str(i) + "일")
listbox.pack(side="left")

scrollbar.config(command=listbox.yview) # listbox는 yscrollcommand를 통해, scrollbar는 config를 통해 서로를 매핑 
root.mainloop()