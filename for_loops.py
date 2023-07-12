#Counting to Twenty:

for number in range(1,21):
    print(number)

# List comprehension
one_through_twenty = [i for i in range(1,21)] 
print(one_through_twenty)

#Make a list of the numbers from 1 - 1_000_000 and then use a for loop to print the numbers

# for number in range(1,1_000_000):
#     print(number)

#Summing a million: make a list of the numbers for one to 1_000_000 and then use min() and max() and sum()

one_through_million = list(range(1,1_000_001))
print(sum(one_through_million))
print(min(one_through_million))
print(max(one_through_million))

#Odd numbers: use the third argument of the range() function to make a list of the odd numbers from 1 to 20 Use a for loop to print each number

odds = list(range(1,20,2))
for i in odds:
    print(i)

#Threes: make a list of the multiples of 3, from 3 to 30 use a for loop to print the numbers in your list

multiples_of_three = list(range(3,31,3))
for i in multiples_of_three:
    print(i)

#Cubes: A number raised to the third power is called a cube: For example the cube of 2 is written as 2**3 in python. 
#Make a list of the first 10 cubes then use a for loop to print each of these values

cubes = [i ** 3 for i in range(1,11)]
for i in cubes:
    print(i)

