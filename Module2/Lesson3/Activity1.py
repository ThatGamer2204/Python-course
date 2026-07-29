total_chores=4
chores_completed=0
chore_num=1
task=""

while chore_num<=total_chores:
    if chore_num==1:
        task="Make your bed"
    elif chore_num==2:
        task="Feed the pets"
    elif chore_num==3:
        task="Water the plants"        
    else:
        task="Buy groceries"
    task_completed=input(f"Have you done the task {task}?").strip().lower()
    if task_completed=="yes":
        chores_completed+=1
        chore_num+=1
    else:
        print(f"Do the task {task}!")
print("You have sucessfully finished all 4 chores !😊")
