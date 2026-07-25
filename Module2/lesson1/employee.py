dept=input("Enter employee department :").strip().lower()
years=int(input("Number of years of experience :"))
prate=int(input("Enter employee performance rating(1~5) :"))
salary=float(input("Enter employee salary :"))
attendance=int(input("Enter employee attendance percentage :"))
bonus=0
if attendance>=90:
    if dept == "sales":
        if prate>=4:
            if years>=5:
                print("20% Bonus")
                bonus=20
            else:
                print("10% Bonus")
                bonus=10
    elif dept=="it":
        if prate == 5 :
            if years>=3:
                print("18 % Bonus")
                bonus=18
            else:
                print(" 12% Bonus")
                bonus=12
    elif dept=="hr":
        if prate>=4:
            if years >=5:
                print("15% Bonus")
                bonus=15
            else:
                print("8% Bonus")
                bonus=8
    salary=((bonus/100)*salary)+salary
    print(f"Your salary with bonus is ${salary}.")
else:
    print("No Bonus for you, at this point, do you even work here?😭🙏")
