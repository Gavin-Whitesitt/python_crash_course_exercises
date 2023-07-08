#Gavin Whitesitt 7/8/23: This is a simple excersise that demonstrates the usage of whitespace characters such as \t and \n 
#it also demonstrates how to use the .removeprefix() method

print("Python")

print("\tPython")

print("\tLanguages: \n\tPython \n\tC \n\tJavascript")

language = 'python '
print(language)

print(language.rstrip())

# removing prefixes

ivyzenith_url = "https://ivyzenith.com"
print(ivyzenith_url.removeprefix('https://'))


