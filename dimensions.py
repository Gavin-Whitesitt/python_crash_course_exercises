#Tuple practice, Let's say that we have a rectangle that should always
#be a certain size. We can ensure that it's dimensions stay the same by
#putting them in a tuple

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#The below commented out code will throw a type error because an element
#in a tuple cannot be changed
#dimensions[0] = 250

#You can loop through values in a tuple using a for loop

for dimension in dimensions:
    print(dimension)

#You cannot modify a tuple, but you can assign a new value to a variable
#Sthat was representing a tuple ex:

dimensions = (400, 100)

print(dimensions)

