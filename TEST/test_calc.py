operator=input("Enter what operation you want to do(+,-,*,/) : ")
op=True
while op==True:
    if operator not in["+","-","*","/"]:
        print("Please enter one of 4 arithmetic operators only")
        operator=input("Enter what operation you want to do(+,-,*,/) : ")
    else:
        op=False

try:
    n1=float(input("Enter first number : "))
except ValueError:
    print("Please enter a number only")
    n1=float(input("Enter first number : "))

try:
    n2=int(input("Enter second number : "))
except ValueError:
    print("Please enter a number only")
    n2=float(input("Enter second number : "))

def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mtp(n1,n2):
    return n1*n2

def div(n1,n2):
    try:
        return n1/n2
    except ZeroDivisionError:
        print("Not defined(N/A)")
if operator=="+":
    print(add(n1,n2))
elif operator=="-":
    print(sub(n1,n2))
elif operator =="*":
    print(mtp(n1,n2))
elif operator == "/":
    print(div(n1,n2))