import random
secret=random.randrange(1,50)
heart=5
ty=1
win=0
while ty<=5:
    guess=int(input("Enter your guess :"))
    if guess==secret:
        print("YOU WON!, secret number was",secret,"\nREMAINING HEARTS :","❤️"*(heart))
        win=1
        break
    elif +(secret-guess)>25:
        print("Proximity level :🧊(Ice cold)\nREMAINING HEARTS :","❤️"*(heart))
    elif +(secret-guess)>=15:
        print("Proximity level :🥶(Cold)\nREMAINING HEARTS :","❤️"*(heart))
    elif +(secret-guess)>=10:
        print("Proximity level :🌡️(Warm)\nREMAINING HEARTS :","❤️"*(heart))
    elif +(secret-guess)>=5:
        print("Proximity level :🔥(Hot)\nREMAINING HEARTS :","❤️"*(heart))
    ty+=1
    heart-=1
if win ==0:
    print(f"All guesses were wrong, secret number is,{secret}.\nREMANINING HEARTS : 0")
            
    
