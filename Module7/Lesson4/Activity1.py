from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename
window=Tk()
window.title('Event Handler')
window.geometry('500x500')
t1=Text(window)
t1.pack()
def open_file():
    filepath=askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    JR=open(filepath,"r")
    Tohoku=JR.read()
    t1.delete(1.0,END)
    t1.insert(END,Tohoku)
    JR.close()
def save_file():
    filepath=asksaveasfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],defaultextension="txt")
    if not filepath:
        return
    JR=open(filepath,"w")
    B=t1.get(1.0,END)
    JR.write(B)
    JR.close()
b2=Button(text="SaHvE fIlE",command=save_file,height=1,width=20,fg="blue",bg="white")
b2.pack()
b1=Button(text="OhPeN fIlE",command=open_file,height=1,width=20,fg="blue",bg="white")
b1.pack()
window.mainloop()