        total_homework=4
        homework_completed=0
        homework_num=1
        hw=""

        while homework_num<=total_homework:
            if homework_num==1:
                hw="Make your bed"
            elif homework_num==2:
                hw="Feed the pets"
            elif homework_num==3:
                hw="Water the plants"        
            else:
                hw="Buy groceries"
            homework_completed=input(f"Have you done the task {task}?").strip().lower()
            if homework_completed=="yes":
                homework_completed+=1
                homework_num+=1
            else:
                print(f"Do the homework {hw}!")
        print("You have sucessfully finished all 4 homeworks !😊")
