print("========WELCOME TO RIDE BUILDER=========")
print("choose 1 for bike, 2 for car.")
choice=int(input("choose your preferred ride :"))
if choice==1:
    bike_type=int(input("Choose 1 for scooty, 2 for motorbike :"))
    if bike_type==1:
        print("Scooty : top speed 85, petrol 20L, good for short distances.")
    else:
        print("Very good choice, try not to go too fast😭🙏")
elif choice==2:
    car_type=int(input("Choose 1 for Sedan, 2 for SUV :"))
    if car_type==1:
        print("Sedan very good car i guess🤷")
    else:
        print("Solid choice👍")
else:
    print("INVALID CHOICE!!! : choose either one or 2")