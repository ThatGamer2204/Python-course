from tkinter import *
from tkinter import messagebox
class rest_mng_sys:
    def __init__(self,window):
        self.window=window
        self.display_bg()
        fj=Frame(master=window,width=500,height=500,bg="white")
        fj.place(relx=0.5,rely=0.5,anchor='center')
        lbl=Label(master=fj,text="Restaurant Management System",fg="white",bg="green",height=1,width=50,font=("Arial", 20, "bold"))
        lbl.grid(row=0,padx=23,pady=23)
        
        self.menu_items = {

        "FRIES MEAL": 2,

        "LUNCH MEAL": 2,

        "BURGER MEAL": 3,

        "PIZZA MEAL": 4,

        "CHEESE BURGER": 2.5,

        "DRINKS": 1

        }
        self.menu_labels={}
        self.menu_qty={}
        for i,(item,qty) in enumerate(self.menu_items.items(),start=1):
            labul=Label(master=fj,text=f"{item}  (${qty}) :",font=("Arial", 20))
            labul.grid(row=i,column=1,padx=2,pady=2)
        self.exchange_rate=90
    def display_bg(self):
        cv=Canvas(self.window,width=800,height=800)
        cv.pack()
        img=PhotoImage(file="background.png")
        cv.create_image(0,0,anchor=NW,image=img)
        cv.Image=img
window=Tk()
window.title('Restaurant Management')
window.geometry('800x600')
win1=rest_mng_sys(window)
window.mainloop()