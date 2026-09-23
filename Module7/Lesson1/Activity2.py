from tkinter import *
window=Tk()
window.title('Getting started with Widgets')
window.geometry('500x500')
lbl=Label(text="Hey There!",fg="blue",bg="white",height=1,width=50)
lbl.pack()
lbl2=Label(text="Full name :",fg="white",bg="blue")
lbl2.pack()
entry1=Entry()
entry1.pack()
text1=Text(height=5)
def Display_details():
    name=entry1.get()
    global usrnam
    usrnam=name+"Me learn java"
    text1.insert(END,"Hello")
    text1.insert(END,usrnam)
    text1.pack()
b1=Button(text="Begin",command=Display_details,height=1,width=20,fg="blue",bg="white")
b1.pack()
window.mainloop()