with open("/workspaces/gcse-24-27-saymeenhossain/File handling/practiceRead.txt", "r") as file:
    content = file.read()
    print(content)

with open("/workspaces/gcse-24-27-saymeenhossain/File handling/practiceRead.txt", "a") as file:
    file.write("\nThis is a new line")