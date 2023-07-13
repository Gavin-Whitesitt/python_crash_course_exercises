#Cars the py examines the sort() method

#the .sort method alphebetizes a list

cars = ["bmw", "toyota,", "audi", "subaru"]
cars.sort()
print(cars)

#The cars list is now alphebetized and cannot be reverted back to its original order unless that original state had been saved elsewhere

# You can pass the reverse=True argument to the .sort method to sort a list reverse alphebetically 

cars.sort(reverse=True)
print(cars)

#To maintain the original order of a list but present it in a sorted order you can use the sorted() function. 
#This function let's you display the list in a certain order without affecting the actual order of the list.

print(f"Here is the original list: {cars}")

print(f"\nHere is the sorted list: {sorted(cars)}")

print(f"\nHere is the original list again: {cars}")

#Sorting a list alphabetically is more complicated when all values are not lowercase and there are several different ways to interpret capital letters

#the .reverse method will flip the order of the list

#reinitializing the list
cars = ["bmw", "toyota,", "audi", "subaru"]
print(f"\n{cars}")
cars.reverse()
print(f"\n{cars}")

#You can use the len() function to determine the length of a list

print(len(cars))

#Try it yourself excercise: Think of at least five places in the world you would like to visit
#Store these locations in a list in non-alphabetical order

places_to_visit = ['Oslo', 'London', 'Tokyo', 'Amsterdam', 'Milan', 'New York']
print(places_to_visit)

print(sorted(places_to_visit))

print(places_to_visit)

places_to_visit.reverse()
print(places_to_visit)
places_to_visit.reverse()
print(places_to_visit)

places_to_visit.sort()
print(places_to_visit)
places_to_visit.sort(reverse=True)
print(places_to_visit)


#Using slices print the fist three items in the list

print(f"the first three places in the places_to_visit list are: {places_to_visit[:3]}")

#The code below prints three items from the middle of the list by getting the middle index and subtracting 1 from the starting index
#and then adding 2 to the ending index
print(f"Three places fron the middle of the list are {places_to_visit[((len(places_to_visit)//2) -1):((len(places_to_visit)//2) +2)]}")

#printing the last three items

print(f"The last three items in the list are {places_to_visit[-3:]}")
