#Question 1
temperature = int(input("Enter the temperature: "))
weather = input("Is it sunny: ")
if temperature > 15 and weather == "yes":
    print("WOAH, ITS A SWARM OF HEAT!!!")

#Question 2
temperature = int(input("Enter the temperature: "))
weather = input("Is it raining: ")
if temperature < 15 and weather == "yes":
    print("WOAH, ITS POURING HEAVILY!!!")

#Question 3
apples = int(input("How many apples?: "))
if apples <10:
    print("That's cool")
else:
    print("WOAH THAT'S A LOT OF APPLES FOR JUST ONE PERSON!")

#Question 4
age = 20
has_driving_licence = True 
if age > 18 and has_driving_licence:
    print("You will have a driving licence as your over 18")
else:
    print("You will not have a driving licence as your under 18")

#Question 5
speed = 60
is_raining = False  
if speed > 60 or not is_raining:
    print("The car is speeding and it is not raining")
else:
    print("The car is not speeding and it is raining")

#Question 6 
hours_studied = 6
feels_prepared = False
if hours_studied > 5 or feels_prepared:
    print("The student has studied enough and feels prepared")
else:
    print("The student has not studied enough and does not feel prepared")

#Question 7
assignments_completed = 6
assignments_pending = 1
if assignments_completed > 5 and assignments_pending < 2:
    print("The student has completed more than 5 assignments and has less than 2 assignments pending")
else:
    print("The student has not completed the current assignments")

#Question 8 
savings = 100
item_price = 120
item_on_sale = True
if savings > item_price or item_on_sale:
    print("You can buy the item")
else:
    print("You can't buy the item")

#Question 9
is_sunny = True
is_weekend = True
if (is_sunny and is_weekend) or (not is_sunny and not is_weekend):
    print("The weather condition matches the day of the week")
else:
    print("The weather condition doesn't match the day of the week")
