#Ordinal numbers indicate their position in a list, such as  1st or 2nd
#All ordinal numbers end in th, except 1, 2 and 3
#Use an if-elif-else chain inside a loop to print the poper ordinal
#ending for each number

numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else: 
        print(f"{number}th")