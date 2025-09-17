# 콤보박스 : 창을 열어 여러 목록 중 하나를 선택
# 콤보박스는 tkinter에서 없고 tkinter.ttk를 import 해야함 
import tkinter.ttk as ttk
from tkinter import * # 티킨터
root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 x 세로

values = [str(i) +'일' for i in range(1,32)] # 1부터 32까지 숫자를 반환
combobox = ttk.Combobox(root, height = 5, values=values)
combobox.pack()
combobox.set("카드 결제일")  # 최초 목록 제목 설정

readonly_combobox = ttk.Combobox(root, height = 5, values=values, state="readonly")
readonly_combobox.current(0) # 0번째 인덱스 값 선택 
readonly_combobox.pack()
readonly_combobox.set("카드 결제일")  # 최초 목록 제목 설정
def btncmd():
   print(combobox.get())
   print(readonly_combobox.get())
btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()