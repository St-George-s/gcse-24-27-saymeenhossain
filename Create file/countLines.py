with open("/workspaces/gcse-24-27-saymeenhossain/Create file/holiday.txt", "r") as file:
    counter = 0
    for line in file:
        print(line) 
        counter = counter + 1
    print("There are", counter, "lines")