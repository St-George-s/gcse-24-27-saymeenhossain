import random

lettersGuessed = []
words = ["apple", "banana", "grape", "strawberry", "mango", "blueberries", "avocado"]
randNum = random.randint(0,6)
#print(randNum)
selectedWord = words[randNum]
print(selectedWord)

userLetter = input("Enter a letter: ")
lettersGuessed.append(userLetter)


found = False
for i in range(len(selectedWord)):
    if selectedWord[i] == userLetter:
        found = True

if found:
    print("letter found")
else:
    print("letter not found")