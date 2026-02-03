password = input("Enter a password: ")
while len(password) < 8:
    print("Password too short")
    password = input("Enter a password: ")


upperCase = 0
lowerCase = 0


while upperCase == 0:
    for letter in password:
        if ord(letter) >= 65 and ord(letter) <= 90:
            upperCase = upperCase + 1
    if upperCase == 0:
        print("You need a uppercase letter, re-enter your password.")
        password = input("Enter a password: ")

while lowerCase == 0:
    for letter in password:
        if ord(letter) >= 97 and ord(letter) <= 122:
            lowerCase = lowerCase + 1
    if lowerCase == 0:
        print("You need a lowercase letter, re-enter your password.")
        password = input("Enter a password: ")

passwordAgain = input("Please enter your password again: ")
while passwordAgain != password:
    print("That is not the same password, try again.")
    passwordAgain = input("Please enter your password again: ")
if ord(letter) >= 33 and ord(letter) <= 64:
    print("Your password is strong :)")
elif len(password) >= 10:
    print("Your password is medium strength :/")
else:
    print("Your password is weak :(")

print("YOUR PASSWORD HAS BEEN RESET!!!!!")