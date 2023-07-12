#Make a list containing the square of the first 5 numbers

first_five_numbers = list(range(1,6))
square_numbers = []

for number in first_five_numbers:
    square_numbers.append(number ** 2)

print(square_numbers)

#You can also use the min() max() and sum() functions within python when working with a list of numbers.

digits = list(range(0,10))
print(min(digits))
print(max(digits))
print(sum(digits))
