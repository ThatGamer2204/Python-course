from tkinter import *
window=Tk()
window.title('Getting started with Widgets')
window.geometry('500x500')
window.mainloop()
obj=Label(text="Hey There!",fg="blue",bg="white",height=1,width=50)
obj.pack()
window.mainloop()