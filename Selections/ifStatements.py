#Question 1
age = int(input("Enter an age: "))
if age > 18: 
    print("You are eligible to watch 18-rated movies")
else:
    print("You are not eligible to watch 18-rated movies")

#Question 2
age = int(input("Enter an age: "))
if age >= 18:
    print("You can watch 18 rated movies")
elif age >= 15:
    print("You can watch 15 rated movies")
else:
    print("You can't watch 18 or 15 rated movies")

#Question 3
emotion = input("Enter an emotion: ")
if emotion == "sad":
    print("Eat some food to make you happy :)")
elif emotion == "angry":
    print("Take anger management classes :<")
elif emotion == "happy":
    print("There is nothing i can do :(")

#Question 4
genre = input("Enter a genre: ")
if genre == "fantasy":
    print("You should watch NARNIA")
elif genre == "horror":
    print("You should watch THE CONJURING")
elif genre == "mystery":
    print("You should watch BLINK TWICE")
else:
    print("I have no recommendations FOR YOU")

#Question 5
number1 = float(input("Enter a number: "))
number2 = float(input("Enter another number: "))
operation = input("Enter and operation: (+ - / *)")
if operation == ("+"):
    print(number1 + number2)
elif operation == ("-"):
    print(number1 - number2)
elif operation == ("/"):
    print(number1 / number2)
elif operation == ("*"):
    print(number1 * number2)