#Many times you will want to to create a new list by leveraging an existing list (or two).

# You can copy an entire list by including the entire list and and omitting the first and second index

my_foods = ['pizza', 'falafel', 'carrot cake' ]
friends_food = my_foods[:]

print(f"My favorite foods are: {my_foods}")
print(f"My friends's favorite foods are: {friends_food}")

my_foods.append("taco")
friends_food.append('steak')

print(f"My favorite foods are: {my_foods}")
print(f"My friends's favorite foods are: {friends_food}")

#If we do not use a silce python would not produce two separate lists. 

#ex: this will not produce the same result

my_foods = ['pizza', 'falafel', 'carrot cake']

# This doesn't work:
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

