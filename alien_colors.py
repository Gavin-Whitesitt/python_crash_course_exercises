#Imagine an alien was just shot down in a game. Create a variable called 
#alien_color and assign it a value of 'green', 'yellow', or 'red'.
#Write and if statement to test if the alien's color is green if it is
#print a message that the player just earned 5 points. Write one version
#of this program that passes and another that fails

alien_color = "red"
#alien_color = "green"
points = 0

if alien_color == "green":
    points = points + 5
else:
    points = points - 2

print(f"You have {points} points.\n")

#Choose a color for an alien as you did previously and write an if-else 
#chain: If the alien's color is green print a statement that the player 
#just earned 5 points for shooting the alien. If the color isn't green 
#print a stetment that the player just lost 2 points
print("starting new game")

alien_colors = ["green","blue","yellow","red"]
points = 0

for alien_color in alien_colors:
    print(f"You shot the {alien_color} alien.")
    if alien_color == "green":
        print("You shot the green alien and have been awarded 5 points")
        points = points + 5
    elif alien_color == "yellow":
        print("You shot the yellow alien and have been awarded 10 points")
        points = points + 10
    elif alien_color == "red":
        print("You shot the red alien and have been awarded 15 points")
        points = points + 15    
    else:
        print("You shot the wrong alien and have lost 2 points")
        points = points - 2
    print(f"You now have {points} points")
