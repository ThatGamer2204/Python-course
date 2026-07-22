day=input("What day of the week is it?").lower()
hw=input("Have you done your homework?").lower()
weather=input("What is the weather?").lower()
print(f"=======YOUR PLAN FOR {day}========")
print("-x"*40)
if day in("saturday","sunday"):
    print("Its a weekend, enjoy your freetime!")
elif day =="monday":
    print("First day of the week, pack your bag")
elif day=="friday":
    print("Last day of school, enjoy")
elif day in("tuesday","wednesday","thursday"):
    print("Regular school day, stay focused")
else:
    print("Daytype not recognized, please give proper day")
if weather=="sunny"and hw=="yes":
    print("Adter school, head to the park!")
elif weather=="rainy" or weather=="cloudy":
    print("Pack your umbrella")
if not (hw=="yes"):
    print("Finish homework before going out.")
if weather=="sunny"and hw=="yes" and day not in("saturday","sunday"):
    print("Best plan, all set for a great school day, you are prepared.")


