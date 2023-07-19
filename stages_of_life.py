#if elif chain determining a person's stage of life. sel a value for age

ages = list(range(0,90,2))
ages.insert(1,1)

for age in ages:
    print(f"Your age is {age}.")
    if age < 2:
        print("You're a baby.")
    elif age < 4:
        print("You're a toddler.")
    elif age < 13:
        print("You're a kid.")
    elif age < 20:
        print("You're a teenager.")
    elif age < 65:
        print("You're an adult.")
    else:
        print("Well you must be an elder.")
    print("\n")