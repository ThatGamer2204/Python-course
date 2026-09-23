from tkinter import *
window=Tk()
window.title('Getting started with Widgets')
window.geometry('500x500')
lst=[[9,8,7],[6,5,4],[3,2,1],["#",0,"*"]]
for i in range(4):
    window.columnconfigure(i,weight=1,minsize=70)
    window.rowconfigure(i,weight=1,minsize=50)
    for j in range(3):
        eframes=Frame(master=window,relief=SUNKEN,borderwidth=5)
        eframes.grid(row=i,column=j)
        lbl=Label(master=eframes,text=lst[i][j],fg="blue",bg="white",height=1,width=10)
        lbl.pack()
window.mainloop()