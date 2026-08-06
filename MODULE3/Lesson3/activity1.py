def calculate_change(paid,price):
    change=paid-price
    return change
snack_price=25
coin_lst=(1,5,10,25)
print("Accepted coin values are 1,5,10,25.\nSnack price is :",snack_price)
total=0
total_coins=0
while True:
    coin=int(input("Enter a coin :"))
    if coin not in coin_lst:
        print("Invalid coin, please enter 1,5,10 or 25 coin")
        continue
    else:
        total+=coin
        total_coins+=1
        print(f"So far, total coins inserted is {total_coins} and total amount is {total}.")

        if total>=snack_price:
            break

change=calculate_change(total,snack_price)
if change==0:
    pass
else:
    print("The change is :",change)
    print(f"Snack Price : {snack_price}\nCoins inserted : {total_coins}\nTotal paid ammount : {total}\nChange : {change}")
    print("THANK YOU FOR YOUR PURCHASE")

    