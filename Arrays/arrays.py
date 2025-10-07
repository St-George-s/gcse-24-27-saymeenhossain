# Create arrays
heights = [2.4, 3.8, 0.4]
names = ["Bob", "Dave", "Simon"]

print(names[1]) # Prints Dave
print(heights[1]) # Prints 3.8

# Loop over names array and print
for counter in range(len(names)):
    print(names[counter]) # Counter is 0 then 1 then 2
    print(heights[counter])

# Append (Add) to array
heights.append(2.2)
names.append("Jimmy")

print(heights)
print(names)