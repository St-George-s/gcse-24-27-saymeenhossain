# Find the area of a rectangle (function)

def getAreaRectangle(length, breadth):
    return length * breadth

# Call a subprogram
print("START")

print(getAreaRectangle(10, 10))

returnedArea = getAreaRectangle(10, 20)
print(returnedArea)

secondReturnedArea = getAreaRectangle(10, 30)

if returnedArea > secondReturnedArea:
    print("First area is bigger")