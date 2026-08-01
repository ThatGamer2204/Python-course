total_homework=4
homework_completed=0
homework_num=1
hw=""

while homework_num<=total_homework:
    if homework_num==1:
        hw="Math worksheet"
    elif homework_num==2:
        hw="physics exercise"
    elif homework_num==3:
        hw="Chemistry report"        
    else:
        hw="English project"
    hw_completed=input(f"Have you done the task {hw}?").strip().lower()
    if hw_completed=="yes":
        homework_completed+=1
        homework_num+=1
    else:
        print(f"Do the homework {hw}!")
print("You have sucessfully finished all 4 homeworks !😊")
