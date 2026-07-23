a=10
b=-10
print(a>>1)
print(b>>2)
print(~a)
print(~b)
print(a|b)
print(a&b)
print(~15)

mark1=float(input("Enter first subject marks :"))
mark2=float(input("Enter second subject marks :"))
mark3=float(input("Enter third subject marks :"))
mark4=float(input("Enter fourth subject marks :"))
mark5=float(input("Enter fifth subject marks :"))

total=mark1+mark2+mark3+mark4+mark5
avg=total/5
print("Total :",total,"Average :",avg)

if avg in range(91,101,1):
    print("Grade : A")
elif avg in range(81,91,1):
    print("Grade :B")
elif avg in range(71,81):
    print("Grade :C")
elif avg in range(61,71):
    print("Grade :D")
elif avg in range(51,61):
    print("Grade :E")
elif avg in range(1,51):
    print("Grade :F")