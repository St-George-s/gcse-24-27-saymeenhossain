# Example
def greet(name): 
    return f"Hello, {name}!" 

print(greet("Alice")) 
print(greet("Bob")) 

# Procedure Example 1
def welcome_message():
    print("Welcome to our program!")

welcome_message()

# Procedure Example 2
def display_instructions(): 
    print("Instructions:") 
    print("1. Enter a number") 
    print("2. Choose an operation") 
    print("3. See the result") 

# Function Example 1
def add_numbers(a, b): 
    return a + b 

result = add_numbers(3, 5) 
print(result) 

# Function Example 2
def multiply_numbers(x, y): 
    return x * y 

product = multiply_numbers(4, 7) 
print(product) 

# Building with Conditionals and Loops 
# Procedure with If Statement 
def check_age(age): 
    if age >= 18: 
        print("You are an adult.") 
    else: 
        print("You are a minor.") 

check_age(20) 
check_age(15) 
check_age(12) 
check_age(89) 

#Procedure with a Fixed Loop 
def repeat_message(message, times): 
    for i in range(times): 
        print(message) 

repeat_message("Hello!", 3) 

