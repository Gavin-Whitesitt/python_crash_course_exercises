#At this amusment park:
#Admission for anyon under age 4 is free. 
#Admission for anyone between the ages of 4 and 18 is $25. 
#Admission for anyone age 18 or older is $40.

guest_ages = [1, 2, 4, 5, 6, 7, 10, 15, 18, 19, 20, 55, 60]

for guest_age in guest_ages:
    print(f"Determining admission cost for guest of age {guest_age}")
    if guest_age < 4:
        price = 0
    elif guest_age >= 4 and guest_age < 18:
        price = 25
    else: 
        price = 40
    print(f"Your admission is ${price}")
    
    

    