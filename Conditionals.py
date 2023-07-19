#Create 10 conditionals and predicit how they will evaluate 

#Equalitys with strings

car = "subaru"
car_2 = "toyota"
car_3 = "Subaru"

if car == car_2:
    print("these cars are the same")
else:
    print("These cars are not the same")

print(car == car_3)
print(car.lower() == car_3.lower())

#Is an item in a list 

groceries = ["apple", "banana", "coconut", "ketchup"]

print("is apple not in the groceries list?")
test = 'apple' not in groceries

print(test)