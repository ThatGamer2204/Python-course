n=int(input("Enter number :"))
order=""
for i in range(n,0,-1):
    s=str(i)
    if i ==1:
        order=order+s
    else:
        order=order+s+">"

print(order)
