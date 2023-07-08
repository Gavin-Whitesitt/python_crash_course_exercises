#name_cases.py is an excercise to build proficency on several different string methods. Follows instructions from Python Crash Course 

tatis_name = "Tatiana"
print(f"hi {tatis_name} welcome to Chili's")

gavins_name = "Gavin Whitesitt"

print(f"{gavins_name.upper()} \n{gavins_name.lower()} \n{gavins_name.title()}")

#Famous Quotes

famous_quote = "One good girl is worth a thousand bitches."
famous_author = "albert einstein"

print(f'{famous_author.title()} once said, "{famous_quote}"')

#Stripping Names 

persons_name = " \t alberto Balsaim\n "
print(persons_name)

print(persons_name.strip().title())
print(persons_name.rstrip().title())
print(persons_name.lstrip().title())

#File Extensions 
#python has a method removesuffix()

filename = 'python_notes.txt'

print(filename.removesuffix('.txt'))

