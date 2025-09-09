# Data Types
name = "Saymeen" #This is a string
myAge = 13 # This is an integer
height = 160 # This is a decimal number (float/real)
hasADriversLicense = False # This is a boolean (True/False)

# Casting (Change from one data type to another)
age = input("Enter age: ")
print(age)
print(age + "10") # Concatenate two strings together (join them)
ageAsAnInt = int(age)
print(ageAsAnInt + 10) # Add two Integers together (maths addition)
print("Your age is " + str(ageAsAnInt))

# Data types - more examples
stillAnInteger = -4
myNumber = "078782282873" # Always store as a string

# Arithmetic operators
add =  10 + 10
subtract = 10 - 10
multiply = 10 * 10
division = 10 / 10 # Will output a float
integerDivision = 11 / 10 # Forces output to be an integer
print(add, subtract, multiply, division)
print(integerDivision)
modulo = 2000 % 501 # Remainder of the division
print(modulo)
exponent = 2 ** 4 # To the power of
print(exponent)

# Activity 1 - Take two inputs, multiply them together and output answer
number1 = float(input("Enter Number: "))
number2 = float(input("Enter Number: "))
print(number1, " X ", number2, " = ", number1 * number2)

# Activity 2 - Input user's age, output age times 7
age = input("Enter age: ")
answer = int(age) * 7
print(answer)

# Activity 3 - Take radius as input, output volume of sphere (v = 4/3 x pi x r^3)
radius = input("Enter radius: ")
volume = 4 / 3 * 3.14159 * float(radius)**3.0
print(volume)