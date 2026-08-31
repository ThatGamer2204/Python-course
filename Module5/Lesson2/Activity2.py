class Employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Destructor called")

def Create_obj():
    print("Making Object")
    emp1=Employee()
    print("Function End")
    return emp1

print("Calling create object()")
obj=Create_obj()

print("Program End")