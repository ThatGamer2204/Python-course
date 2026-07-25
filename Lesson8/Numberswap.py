a=int(input("Enter Number 1:"))
b=int(input("Enter Number 2:"))
c=int(input("Enter Number 3:"))

print(f"Original Numbers are {a},{b} and {c}.")
temp=a
a=c
c=b
b=temp

print(f"Swapped numbers are {a},{b} and {c}.")