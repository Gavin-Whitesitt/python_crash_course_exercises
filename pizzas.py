#Think of a least three kinds of your favorite pizza: Store these in a 
#list then use a for loop to print the name of each pizza

favorite_pizzas = ['Cowboy', 'pepperoni and olive', 'chicken and bbq']

for pizza in favorite_pizzas: 
    print(f"Damn today seems like a good day for a {pizza} pizza.")

print(
"I think that everyone that doesn't like pizza like me shouldn't have the same rights that I do."
     )

#Slice excercise: make a copy of the pizza list called friends_pizza and
#add a new pizza to the original list and add a new pizza to the 
#friends_pizza list

friends_pizzas = favorite_pizzas[:]

favorite_pizzas.append('bacon and tomato')
friends_pizzas.append('pineapple')

print("My favorite pizzas are: ")
for pizza in favorite_pizzas:
    print(pizza)

print("My friends favorite pizzas are: ")
for pizza in friends_pizzas:
    print(pizza) 

