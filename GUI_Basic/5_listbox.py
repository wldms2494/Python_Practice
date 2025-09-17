from tkinter import * # 티킨터
root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 x 세로

listbox = Listbox(root, selectmode="extended", height =0)
# selectmode : 여러개 선택 가능, height 는 0으로 하면 전체 보이고 숫자 지정시 3이면 3개만 보임
listbox.insert(0,"사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박") # END 지정시 숫자를 지정하지 않아도 제일 끝으로 위치
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    # 리스트 값 삭제
    # listbox.delete(0) # 제일 뒷 픽리스트값 삭제, END는 제일 뒷값 삭제
    # 갯수 확인
    #print("리스트에는 ", listbox.size(),"개가 있어요 ")
    # 항목 확인
    print("1번째부터 3번쨰 까지의 항목 : ", listbox.get(0,2)) # .get(시작index, 끝 index)
    #선택된 항목 확인
    print("선택된 항목 : ", listbox.curselection()) # current selection 
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()