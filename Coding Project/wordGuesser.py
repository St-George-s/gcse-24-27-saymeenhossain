import random

lettersGuessed = []
words = ["apple", "banana", "grape", "strawberry", "mango", "blueberries", "avocado"]
randNum = random.randint(0,6)
#print(randNum)
selectedWord = words[randNum]
#print(selectedWord)

userLetter = ""
lettersGuessed.append(userLetter)


blankWord = ""
for x in range (len(selectedWord)):
    blankWord = blankWord + "_"
#print(blankWord)

while selectedWord != blankWord: 
    userLetter = input("Enter a letter: ")
    found = False
    for i in range(len(selectedWord)):
        if selectedWord[i] == userLetter:
            found = True
            #print(i)
            blankWord = blankWord[:i] + userLetter + blankWord[i+1:]
    print(blankWord)
    # if found:
    #     print("letter found")
    # else:
    #     print("letter not found")

print ("WORD GUESSED HORAAYYYYYYYY!!!!")