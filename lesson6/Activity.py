print("====Library visit planner=====")
print("Answer the following questions to plan your library visit 😊")

day=input("Enter the day(Monday to Sunday) :").strip().lower().capitalize()
weather=input("Enter the weather(Sunny/Rainy/Cloudy) :").strip().lower().capitalize()
book=input("Enter yes if book is due, no if no book is due :").strip().lower().capitalize()

print(f"======Your Library plan for {day}=======")
print("-x-"*25)
if day=="Monday":
    print("Day Type = Start of the week, check your reading list.")
elif day=="Friday":
    print("Day Type = Last day of the week, return your books before the weekend.")
elif day in("Saturday","Sunday"):
    print("Day Type = Weekend- A good time for a relaxed library visit.")
elif day in("Wednesday","Tuesday","Thursday"):
    print("Day Type = Regular school day-Plan a short library visit.")
else:
    print("Day Type = Unrecognized day, check your spelling and try again.")


if weather =="Sunny" and book=="Yes":
    print("Library tip= Great Weather! Return your book and borrow a new one.")

if weather == "Rainy"or weather == "Cloudy":
    print("Dont forget to carry an umbrella.")

if not(book=="Yes"):
    print("No book due. No need to return any book.")

if weather =="Rainy"and book=="Yes":
    print("Best Plan = Visit library carefully and return your book on time.")
elif weather=="Sunny"and book=="Yes"and not(day in("Saturday","Sunday")):
    print("Best Plan = Stop by the library after school and return your book.")
elif weather =="Sunny"and day in("Saturday","Sunday"):
    print("Best Plan = Longer reading session at the library.")
else:
    print("Best Plan = Check your schedule and plan a library visit.")
print()
print("Library Plan complete. Happy Reading!")