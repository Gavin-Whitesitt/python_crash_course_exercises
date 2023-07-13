#If you could invite anyone, living or deceased, to dinner, who would 
#you invite
#Make a list to represent this and then use the list to print a 
#personalized invite to each of them

#to acomplish this I decided to make a simple for loop to insert each 
#element from the dinner_invite_list into an invitation using f strings

dinner_invite_list = [
    "Tatiana Arvizu", "Jake Sippy", "Scarlet Nino", 
    "Nathan Park", "Daniel Whitesitt", 
    "Kaitlyn Whitesitt","Preston Crowe"
    ]

for i in dinner_invite_list:
    print(
        f"Dear {i.title()}, please join me for a night of eating good food and hanging with good" 
        "company :]"
        )


#Changing guest list 
#print a message stating who can no longer come to the party 
#modify the list to replace the name of the guest who can no longer make
#it with the name of the new person you are inviting

no_longer_coming = dinner_invite_list.pop(1)

print(
    f'{no_longer_coming} can no longer come to dinner due to extreme IBS symptoms')

#reprinting the set of invite messages for those who can still come
for i in dinner_invite_list:
    print(f"Dear {i.title()}, please join me for a night of eating good food and hanging with good" 
          "company :]"
          )

#More Guests
#You found a bigger dinner table, so now you can invite 3  more guests 
#to your dinner party

dinner_invite_list.insert(0,'Alex Jones')
#len(list) // 2 gives the "middle" index
dinner_invite_list.insert((len(dinner_invite_list) 
                           // 2),'Ballseph Taintlicker')
dinner_invite_list.append('Big Goose')

for i in dinner_invite_list:
    print(
        f"Listen up guests: {i.title()} this is your new invite, just a heads up Ballseph" 
        "Taintlicker is invited so don't bring your girl if you want to keep her..."
        )

#Shrinking Guest List 
#The new table was destroyed in an unfortunate IBS related freeway collision 
#You need to now shrink your guest list to only two people 

print("Sorry guys, Jake crashed into a semi in Kansas and now I can only accomodate two people")

uninvited_message_distribution_list = []

#This while loop should uninvite the last person the dinner_invite_list 
#and then append that peson to the dinner_invite_list until only the 
#first two people on the invite list remain
while len(dinner_invite_list) > 2:
    uninvited_message_distribution_list.append(dinner_invite_list.pop(-1))


for i in uninvited_message_distribution_list:
    print(f"Dear {i.title()}\nSorry, you're out kid")
    
print(f"{dinner_invite_list[0].title()} and {dinner_invite_list[1].title()} you're still invited.")

del dinner_invite_list[0]
del dinner_invite_list[0]

print(dinner_invite_list)

#print a message indicating the number of people I am inviting to dinner
print(f"There are {len(dinner_invite_list)} people invited to dinner now")

