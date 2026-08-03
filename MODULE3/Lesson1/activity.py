def greet_customer():
    print("Welcome to Lemonade store!")

def calculate_total(price,no_cups):
    total=price*no_cups
    return total

def calculate_change(total,amount):
    change=amount-total
    return change

def thank_you():
    print("Thank you for visiting!")

greet_customer()
price=int(input("Enter price per cup :"))
no_cups=int(input("Enter the number of cups :"))
total=float(calculate_total(price,no_cups))
amount=float(input("Enter your total amount given :"))
print(f"The total is :{calculate_total(price,no_cups)}")
print(f"Rounded total is : {round(total)}")
print(f"Change due :{calculate_change(total,amount)}")
print(f"{thank_you()}\nThe total is :{calculate_total(price,no_cups)}\nRounded total is : {round(total)}\nChange due :{calculate_change(total,amount)}")

