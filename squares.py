#a list comprehension allows you to generate what could have taken multiple lines of code and a for loop in a single line of code

#for loop for generating list of squares
numbers_squared = []
for number in range(1,11):
    numbers_squared.append(number ** 2)

print(numbers_squared)

#List comprehension doing the same thing:

squares = [value**2 for value in range(1,11)]
print(squares)

