# Question 11
code = "rzy"
userInput = input("Enter code: ")
while code != userInput:
    print("NO")
    userInput = input("Re-enter code: ")
print("Code accepted")

# Question 12
code = "4003"
userInput = input("Enter code: ")
while code != userInput:
    print("NO")
    userInput = input("Re-enter code: ")
print("Code accepted")

# Question 13
userInput = int(input("Enter code: "))
while userInput <= 14:
    print("NO")
    userInput = int(input("Re-enter code: "))
print("Age accepted")

# Question 14 
password = input("What is your password?: ")
while len(password) < 5:
    password = input("AGAIN, What is your password?: ") 
print("Password accepted") 

#Question 15
anotherEpisode = input("Would you like to watch another?")
while anotherEpisode == "yes":
    print ("Playing another")
    anotherEpisode = input("Would you like to watch another?")

print("Good, go to bed :)")

#Question 16
money = input("Enter amount of money: ")
while int(money) >100:
    money = money + int(input("Enter amount of money: "))

print("I accept your offer")
print("You gave me," money)