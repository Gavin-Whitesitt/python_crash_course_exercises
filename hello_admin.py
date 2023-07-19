#Make a list of five or more usernames, including the name "admin"
#loop through the list and print a greeting to each user if the username
#is admin print a special greeting

usernames = ["admin", "gavin", "taintlicker2000", "reee"]
#usernames = []

if usernames:
    for username in usernames:
        if username == "admin":
            print("Hello bossman, try not to nuke the server.")
        else:
            print(f"Hello {username}, welcome to the website")
else:
    print("There are no users")

#Create a program that simulates how websites ensure that everyone has a
#unique username

current_usernames = usernames[:]

username_user_inputs = ["rolobones63", "gavin", "johnson", " Admin"]


for username_user_input in username_user_inputs:
    if username_user_input.strip().lower() in current_usernames:
        print("Sorry that username is already taken.")
    else:
        current_usernames.append(username_user_input.strip().lower())

print(current_usernames)

