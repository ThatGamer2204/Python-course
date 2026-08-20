dayz=(1,0,0,1,0,0,1)
sunny,rainy=0,0
for i in dayz:
    if i==1:
        rainy+=1
    else:
        sunny+=1
if sunny>rainy:
    print("Good weather")
else:
    print("Bad weather")