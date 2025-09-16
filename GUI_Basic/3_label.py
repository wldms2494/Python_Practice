from tkinter import * # 티킨터
root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 x 세로

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="GUI_Basic/image.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")
    global photo2
    photo2 = PhotoImage(file="GUI_Basic/image2.png")
    label2.config(image=photo2)
btn = Button(root, text="클릭", command = change)
btn.pack()

root.mainloop()