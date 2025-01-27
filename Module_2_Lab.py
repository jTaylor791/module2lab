"""
Name: Jonah Taylor
File Name: Module_2_Lab
Description: Will ask the user for his last name which can be exited by entering ZZZ or continues and asks the users first name as well an gpa. It will then report if they have made the Honor Roll or Dean's List
"""
lastInput = input("Enter your last name: ")
if lastInput != "ZZZ":
    firstInput = input("Enter your first name: ")
    gpaInput = input("Enter your GPA as a float: ")
    if gpaInput > 3.5:
        print(firstInput + " has made the Dean's List")
    elif gpaInput > 3.25:
        print(firstInput + " has made the Honor Roll")