try:
    n1=int(input("Enter number 1 :"))
    n2=int(input("Enter number 2 :"))
    div=n1/n2

except ValueError:
    print("Enter a valid whole number.")
except ZeroDivisionError:
    print("Division by Zero is an Error!!")
except:
    print("Wrong input")
else:
    print("No Exceptions")
finally:
    print("This will execute no matter what.")