total_homework=4
homework_completed=0
hw_num=1
hw=""

while hw_num<=total_homework:
    if hw_num==1:
        hw="Maths worksheet"
    elif hw_num==2:
        hw="English project"
    elif hw_num==3:
        hw="Physics problems"        
    else:
        hw="Chemistry report"
    hw_completed=input(f"Have you done the hw {hw}?").strip().lower()
    if hw_completed=="yes":
        homework_completed+=1
        hw_num+=1
    else:
        print(f"Do the hw {hw}!")
print("You have sucessfully finished all 4 homeworks !😊")
