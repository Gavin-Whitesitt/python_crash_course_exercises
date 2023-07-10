motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)


#Assigns the first element in the list to the string 'ducati'
motorcycles[0] = 'ducati'
print(motorcycles)

#The below code will not work because the 4th and 5th element in the list is out of range
#motorcycles[4] = 'test'
#motorcycles[3] = 'test'

#if we would like to add additonal elements to a list we can use the .append method

motorcycles.append('honda')
print(motorcycles)

#the below code will not work because the .append method only accepts one argument
#motorcycles.append('one', 'two')

#It is common the define empty lists and have users populate them using the .append method

#You can also use the insert() method which is similar to using list[x] execpt insead of replacint the element in the list it shifts 
#the remaining elements to the right

motorcycles.insert(0, 'toyota')
print(motorcycles)

#Removing elements from a list 

#If you know the position of the item you want to remove you can use the del statement

del motorcycles[0]
print(motorcycles)

#You can also remove an element in a list usint the pop() method, if no argument is given it will take the last item from the list

#the pop method lets you remove an element but it still stores it for usage at a later point

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

print(f'The last motercycle in the list was a {popped_motorcycle.title()}, that was before I popped it.')

#We can also specify a value to pop by specifying the index of the element in the list we are trying to reference 

first_motorcycle = motorcycles.pop(0)

print(f'The first motorcycle I put in that list was a {first_motorcycle.title()}, but then I popped it. Because I get it popping.')

#Removing an item by value

#Sometimes you won't know the position of the item in the list that you need to remove but you do know the value.
#The .remove method works by referenceing the element in the list by it's value instaed of it's position

#Starting with a fresh list
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'

motorcycles.remove(too_expensive)
print(motorcycles)
print(f"I removed {too_expensive.title()} from the motorcycles list because it was too expensive. (Let's just pretend lol)")

#Let's expiriment to see what happens if I give the .remove method a list of values

#remove_list = ['honda', 'suzuki']
#motorcycles.remove(remove_list)

#This doesn't work because the .remove method is expecting a single value, I have an intuition that if the list motorcycles
#had an element that was a list that had those values it would have worked. Let's expiriment:

motorcycles_spare = [['honda', 'suzuki'], 'yamaha', 'suzuki', 'ducati']
remove_list = ['honda', 'suzuki']
print(motorcycles_spare)

motorcycles_spare.remove(remove_list)
print(motorcycles_spare)
del motorcycles_spare

#Hey, see sometimes my intuition is right :)

#Note: the remove() method only delets the first occurrence of the specified value. You can use a loop to ensure all occurrences of the value are removed





