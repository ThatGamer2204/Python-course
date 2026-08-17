import random
playing=True
winner=None
while playing==True:
    player_choice=input("Enter Rock, Paper or Scissor :").strip().lower()
    comp_choice=random.randint(1,3)
    if player_choice=="rock" and comp_choice==2:
        winner="Computer"
    elif player_choice=="rock" and comp_choice==3:
        winner="Player"
    elif player_choice=="rock" and comp_choice==1:
        winner="Tie"
    elif player_choice=="paper" and comp_choice==2:
        winner="Tie"
    elif player_choice=="paper" and comp_choice==3:
        winner="Computer"
    elif player_choice=="paper" and comp_choice==1:
        winner="Player"
    elif player_choice=="scissor" and comp_choice==2:
        winner="Player"
    elif player_choice=="scissor" and comp_choice==3:
        winner="Tie"
    elif player_choice=="scissor" and comp_choice==1:
        winner="Computer"
    elif player_choice=="stop":
        playing=False
        break
    else:
        print("Invalid input, please enter again")
    if comp_choice==1:
        c_choice="Rock"
    elif comp_choice==2:
        c_choice="Paper"
    elif comp_choice==3:
        c_choice="Scissor"

    print(f"The player choice is {player_choice}, the computer choice is {c_choice}, so the winner is :{winner}")
