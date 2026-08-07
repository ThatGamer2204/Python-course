try:
    d=input("Enter a number :")
    nmbr=int(d)
except ValueError as ex:
    print("Exception :",ex)
else:
    print(nmbr)