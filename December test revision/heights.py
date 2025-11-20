totalHeight = 0
counter = 0

for i in range(4):
    userInput = int(input("Enter your height: "))
    totalHeight = totalHeight + userInput
    counter = counter + 1   
print("Average is:", totalHeight / counter)