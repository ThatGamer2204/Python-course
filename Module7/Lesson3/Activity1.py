from tkinter import *
window=Tk()
window.title('Event Handler')
window.geometry('500x500')
def handle_keypress(event):
    print(event.char)
window.bind("<Key>",handle_keypress)
def handle_click(event):
    print("Button is clicked")
b1=Button(text="Click ME",height=1,width=20,fg="blue",bg="white")
b1.pack()
b1.bind("<Button-3>",handle_click)
window.mainloop()