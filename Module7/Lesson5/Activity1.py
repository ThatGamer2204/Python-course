from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename
window=Tk()
window.title('Denomination calculator')
window.geometry('500x500')
t1=Entry(window)
t1.pack()
lbl=Label(text="100 note",fg="white",bg="green",height=1,width=50)
lbl.pack()
lbl2=Label(text="50 note",fg="white",bg="green")
lbl2.pack()
lbl3=Label(text="20 note",fg="white",bg="green")
lbl3.pack()
lbl4=Label(text="10 note",fg="white",bg="green")
lbl4.pack()
lbl5=Label(text="5 note",fg="white",bg="green")
lbl5.pack()
lbl6=Label(text="1 note",fg="white",bg="blue")
lbl6.pack()
t3=Entry(window)
t3.pack()
t4=Entry(window)
t4.pack()
t5=Entry(window)
t5.pack()
t6=Entry(window)
t6.pack()
t7=Entry(window)
t7.pack()
t8=Entry(window)
t8.pack()
def calc():
    t2=t1.get()
    t2=int(t2)
    total_100,total_50,total_20,total_10,total_5,total_1,customers_served,total_dispensed=0,0,0,0,0,0,0,0
    idx=1
    serving=True
    while serving == True:

        if t2<=0:
            q1=Entry(window)
            q1.pack()
            q1.delete(0,END)
            q1.insert(END,"INVALID INPUT")
        else:
            
            remaining=t2
            while idx<=6:
                if idx == 1:
                    value=100
                elif idx == 2:
                    value=50
                elif idx==3:
                    value=20
                elif idx==4:
                    value=10
                elif idx==5:
                    value=5
                elif idx==6:
                    value=1
                count=remaining//value
                remaining-=(count*value)
                if idx == 1:
                    total_100=count
                elif idx == 2:
                    total_50=count
                elif idx==3:
                    total_20=count
                elif idx==4:
                    total_10=count
                elif idx==5:
                    total_5=count
                elif idx==6:
                    total_1=count
                idx+=1
            serving=False
    t3.insert(END,str(total_100))
    t4.insert(END,str(total_50))
    t5.insert(END,str(total_20))
    t6.insert(END,str(total_10))
    t7.insert(END,str(total_5))
    t8.insert(END,str(total_1))
b2=Button(text="Calculate",command=calc,height=1,width=20,fg="white",bg="green")
b2.pack()
#b1=Button(text="OhPeN fIlE",command=open_file,height=1,width=20,fg="green",bg="white")
#b1.pack()
window.mainloop()