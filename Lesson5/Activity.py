temp=float(input("Enter temperature :"))
wind=float(input("Enter wind speed :"))
rain=input("Enter if there is rain or not(Yes/No) :").upper()
puddle=input("Enter if there is puddles or not(Yes/No) :").upper()

if rain=="YES":
    if puddle=="YES":
        print("Bring an umbrella and wear boots")
    else:
        print("Bring umbrella and wear sneakers")
if temp>20:
    print("Wear cool clothes")
else:
    print("Wear normal clothes")
if puddle=="YES":
    print("Wear boots.")
if wind>15:
    print("Wear windbreaker")
else:
    print("Dont wear windbreaker")
