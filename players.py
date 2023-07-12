
players = ['charles', 'martin', 'machael', 'florence', 'eli']
print(players[0:3])

#Above code prints a slice of the list (index 0, 1 and 2)

print(players[1:4])

#If you omit the first index in a slice Python automatically starts your slice at the beginning of the list:
print(players[:4])

#If you want all of the elements from a certain index to the end of a list you can use the syntax list[x:]

print(players[2:])

#You can also use the synax [-x:] to output all of the elements from any point in your list to the end 

print(players[-2:])

#Note, you can include a third value in the brackets idicating a slice to tell python how many items to skip between items in the specified range

print(players[1:4:2]) #The 2 tell python to skip 2 elements after the first element is selected with 1 thus selecting the 3rd element

#Looping through a slice
#Loop through the first 3 players and print a message to them

for player in players[:3]:
    print(f"{player} congrats you are one of the first three players on the roster. This means that we will be feeding you pasta and lobster.")



