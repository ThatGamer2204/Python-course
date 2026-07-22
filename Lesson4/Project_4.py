team1=120
team2=95
team3=140
team4=110
team5=85
 
total = team1 + team2 + team3 + team4 + team5
average = total / 5
 
print("Total points :", total)
print("Average per team :", average)
 
starsperpoint = 2
rewardstars = total * starsperpoint
print("Total reward stars :", rewardstars)
 
boxes = rewardstars // 25
leftover = rewardstars % 25
 
print("Full boxes packed  :", boxes)
print("Leftover stars     :", leftover)
 

last_week = 500
 
print("Better than last week? :", total > last_week)
print("Same as last week? :", total == last_week)
print("At least as good? :", total >= last_week)
 
total += 30
print("After bonus points :", total)
 
total -= 15
print("After missed tasks :", total)
 
reward_stars = total * starsperpoint
boxes = reward_stars // 25
 
print("Final boxes packed :", boxes)
