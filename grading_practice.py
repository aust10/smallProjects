print("Lets get to grading")
def grading():
    user_input= input("What is the grade 0-100? ")
    user_input = int(user_input)

    #grabs the last number of user grade and gives it a above or below
    grade = user_input % 10
    if grade >= 6:
        grade = "+"
    elif grade == 5:
        grade = ""
    else:
        grade = "-"
    
    #below gives the final grade with the above or below
    if user_input >= 90:
        print(f"{grade}A")
    elif user_input >= 80 < 89:
        print(f"{grade}B")
    elif user_input >= 70 < 79:
        print(f"{grade}C")
    elif user_input >= 60 < 69:
        print(f"{grade}D")
    elif user_input >= 0 < 59:
        print(f"{grade}F")
    else:
        print("Invalid answer, Enter a valid number")
        grading()
    answer= input("Do you have more to do? y or n: ")
    if answer == "y":
        grading()
    else:
        print("Thank you for grading with me!")
grading()