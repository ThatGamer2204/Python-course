total_100,total_50,total_20,total_10,total_5,total_1,customers_served,total_dispensed=0,0,0,0,0,0,0,0
idx=1
serving=True
print("========ATM Cash dispenser========\n")
while serving == True:
    name=input("Enter your name :")
    amount=int(input("Enter amount dispensed :"))
    if amount<=0:
        print("INVALID AMOUNT")
    else:
        print(f"MR/MRS {name}, withdrawing {amount}.")
        remaining=amount
        while idx<=6:
            if idx == 1:
                value=100
            elif idx == 2:
                value=50
            elif idx==3:
                value=20
            elif idx==4:
                value=10
            elif idx==5:
                value=5
            elif idx==6:
                value=1
            count=remaining//value
            remaining-=(count*value)
            if idx == 1:
                total_100=count
            elif idx == 2:
                total_50=count
            elif idx==3:
                total_20=count
            elif idx==4:
                total_10=count
            elif idx==5:
                total_5=count
            elif idx==6:
                total_1=count
            idx+=1
        print(f"The total number of notes required are {total_100} notes of 100, {total_50} notes of 50, {total_20} notes of 20, {total_10} notes of 10, {total_5} notes of 5, {total_1} notes of 1.")
        customers_served+=1
        total_dispensed+=amount
        idx=1
        count,remaining,amount=0,0,0
    if total_dispensed>=1000000:
        serving=False
print(f"Customers served :{customers_served}, total amount dispensed :{total_dispensed}")
print("=====ATM Session closed=====\nHave a nice Day!😅")
