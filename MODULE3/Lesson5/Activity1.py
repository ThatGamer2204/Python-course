import random
secret=random.randint(0,9)
playing=True
while playing==True:
    guess=int(input("Enter your guess :"))
    if guess==secret:
        print("YOU WON!, secret number was",secret,)
        playing=False
        break
            
    
