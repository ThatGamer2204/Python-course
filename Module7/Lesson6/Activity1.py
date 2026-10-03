from tkinter import *
from tkinter import messagebox
class rest_mng_sys:
    def __init__(self,window):
        self.window=window
        self.display_bg()
        fj=Frame(master=window,width=150,height=150,bg="white")
        fj.place(relx=0.5,rely=0.5,anchor='center')
        lbl=Label(master=fj,text="Restaurant Management System",fg="white",bg="green",height=1,width=25,font=("Arial", 20, "bold"))
        lbl.grid(row=0,columnspan=3,padx=2,pady=2)
        
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
            t1=Entry(fj,width=10)
            t1.grid(row=i,column=2,padx=2,pady=2)
            self.menu_labels[item]=labul
            self.menu_qty[item]=t1
        labul2=Label(master=fj,text="CuRrEnCy",height=1,width=25,font=("Arial", 20, "bold"))
        labul2.grid(row=8,column=1,padx=2,pady=2)
        self.exchange_rate=90
        self.currency_var=StringVar()
        currency_dropdown=OptionMenu(fj,self.currency_var,"USD","INR")
        currency_dropdown.grid(row=8,column=2,padx=2,pady=2)
        self.currency_var.set("USD")
        self.currency_var.trace_add("write",self.update_labuls)
        b1=Button(master=fj,command=self.place_order,text="PlAhCe OrDhEr",height=1,width=20,fg="blue",bg="white")
        b1.grid(row=9,columnspan=3,padx=2,pady=2)
    def place_order(self):
        cuhrenshy=self.currency_var.get()
        if cuhrenshy=="USD":
            symbol="$"
            self.exchange_rate=1
        else:
            symbol="₹"
            self.exchange_rate=90
        cowst=0
        for mehungry,qty in self.menu_qty.items():
            food_qty=int(qty.get())
            cowst=((self.menu_items[mehungry]*self.exchange_rate)*food_qty)+cowst
        print(cowst)
    def update_labuls(self,*args):
        cuhrenshy=self.currency_var.get()
        if cuhrenshy=="USD":
            symbol="$"
            self.exchange_rate=1
        else:
            symbol="₹"
            self.exchange_rate=90
        for item,llabel in self.menu_labels.items():
            llabel.configure(text=f"{item}  ({symbol},{self.menu_items[item]*self.exchange_rate}) :")
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