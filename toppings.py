requested_toppings = ["mushrooms","extra cheese","green peppers"]

if "anchovies" not in requested_toppings:
    print("Hold the the anchovies!")

if "mushrooms" in requested_toppings:
    print("adding mushrooms")
if "pepperoni" in requested_toppings:
    print("adding pepperoni")
if "extra cheese" in requested_toppings:
    print("adding extra cheese.")
print("pizza is done \n")
#We are out of green peppers
for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"adding {requested_topping} to the pizza!")

print("pizza is done.\n")

#Checking for an empty list:

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == "green peppers":
            print("Sorry, we are out of green peppers right now.")
        else:
            print(f"adding {requested_topping} to the pizza!")
else:
    print("Are you sure you want a plain pizza?")
print("\n")

#Using multiple lists:

available_toppings = ["mushrooms", "olives", "geen peppers", 
                      "pepperoni", "pineapple","extra cheese"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping} to pizza!")
    else: 
        print(f"Sorry we don't serve {requested_topping} here.")
print("order up \n")

