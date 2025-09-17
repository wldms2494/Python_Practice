# 프로그레스바 역시 ttk 에서 생성 가능 
import time
import tkinter.ttk as ttk
from tkinter import * # 티킨터
root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 x 세로

# progressbar = ttk.Progressbar(root, maximum = 100, mode="determinate") # indeterminate 불확정 
# progressbar.start(10) # 10ms 마다 움직임  
# progressbar.pack()

# def btncmd():
#    progressbar.stop() # 작동중지
# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101): # 1 ~ 100
        time.sleep(0.01)  # 0.01초 대기, import time 해줘야함

        p_var2.set(i)  # 실제 Progressbar의 값을 설정
        progressbar2.update() # UI 업데이트
        # 얘를 안넣으면 for문 다 돌고 GUI에 업데이트 되기 때문에 bar가 한번에 올라간것 처럼 보임. for문 돌때마다 GUI를 업데이트 해주는 구문을 추가
        print(p_var2.get())

btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()