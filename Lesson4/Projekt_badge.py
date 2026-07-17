name=input("Enter the school club member name :")
club=input("Enter the school club name :")
memberno=1242423
points=2325
event_count=12
hours=123.5
is_active=True
#BAdge:
print("Member name :",name,type(name))
print("Club name :",club,type(club))
print("Member number :",memberno,type(memberno))
print("Points Earned :",points,type(points))
print("Number of Events :",event_count,type(event_count))
print("Number of Hours :",hours,type(hours))
print("Member Status :",is_active,type(is_active))

memberno=str(memberno)
points=str(points)
event_count=str(event_count)
hours=str(hours)
is_active=str(is_active)

badgecode=name[0:3]+name[-1]

secretcode=club[::-1]
print("Badge Code :",badgecode)
print("Reversed Club name :",secretcode)
badgeline1="CLUB MEMBER"+badgecode.upper()
badgeline2="ID :"+memberno+"| EVENTS: "+event_count
badgeline3="POINTS: "+points+"| ACTIVE: "+is_active
badgeline4="SECRET CLUB CODE :"+secretcode.upper()


print("")
print("========= SCHOOL CLUB MEMBER BADGE =========")
print(badgeline1)
print(badgeline2)
print(badgeline3)
print(badgeline4)
print("============================================")