from tkinter import *
from tkinter import messagebox
window=Tk()
window.title('Event Handler')
window.geometry('200x200')
def msg():
    messagebox.showwarning("Alert!","Stop! Virus found")
b1=Button(text="Scan for Virus",command=msg,height=1,width=20,fg="blue",bg="white")
b1.place(x=40,y=80)
window.mainloop()