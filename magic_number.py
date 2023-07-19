answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again.")

ages = list(range(0,10))

print("You have to be between 3 and 7 to get a free game.")
for age in ages:
    print(f"{age} is being tested")
    if age < 3:
        print("You are to young to get a free game")
    elif age > 7:
        print("You are too old to get a free game")
    else:
        print("You get a free game!")
    print("\n")

#Another implementation:

print("You have to be between 2 and 4 to get a free game")
for age in ages:
    if age <= 4 and age >= 2:
        print(f"Because you are {age} that means you are between 2 and 4. You get a free game. :)")
    else:
        print(f"Because you are {age} you're not between 2 and 4. Sorry you don't get a free game")

#Expiriments with or logic

print("You either have to be over 6' tall or make over $150,000 to enter this club.")

men_heights_and_salary = [[6,140_000], [5.4, 210_000], [5.9, 70_000]]

for man in men_heights_and_salary:
    print(f"You're {man[0]} tall and you make {man[1]}")
    if man[0] >= 6 or man[1] >= 150_000:
        print("Welcome to the club")
    else:
        print("Sorry you're too short, and you also don't make enough money")

#The average height in your group has to be 6' and the median weight in
#your group has to be between 160 and 180. You also need at least one 
#guy who has been to a joeyy concert

winco_aficionados = {
    "Name": ["Preston","Jake", "Gavin"], 
    "Height": [5.8,5.9,6.3],
    "Weight": [100, 165, 220],
    "joeyy_concert": [True, False, False]
    }

print(f"Okay, {winco_aficionados['Name']}...")
if sum(winco_aficionados["Height"]) / len(winco_aficionados["Height"]) == 6 and (
        sorted(winco_aficionados["Weight"])[len(winco_aficionados["Weight"])//2] > 160 
        and sorted(winco_aficionados["Weight"])[len(winco_aficionados["Weight"])//2] < 180  
        ) and True in winco_aficionados["joeyy_concert"]:
    print("Welcome to the club")
else:
    print("Get out of here. Immediately!\n\t Go on get!") 
        
#