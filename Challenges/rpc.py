import random

while True:
    print("----------")
    user_choice = input("Pick Rock, Paper, or Scissors: ")
    print("----------")
    if user_choice == ("Rock"):
        print("You chose Rock")
    elif user_choice == ("Paper"):
        print("You chose Rock")
    elif user_choice == ("Scissors"):
        print("You chose Rock")
    else:
        print("This is not a valid input, please try again.")


    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        computer_choice_str = "Rock"
    elif computer_choice == 2:
        computer_choice_str = "Paper"
    elif computer_choice == 3:
        computer_choice_str = "Scissors"

    print("The computer chose: " + computer_choice_str)
    print()

    if user_choice == ("Rock") and computer_choice_str == ("Rock"):
        print("Draw")

    if user_choice == ("Rock") and computer_choice_str == ("Paper"):
        print("The computer wins! :(")

    if user_choice == ("Rock") and computer_choice_str == ("Scissors"):
        print("The user wins! :)")

    if user_choice == ("Paper") and computer_choice_str == ("Rock"):
        print("The user wins! :)")

    if user_choice == ("Paper") and computer_choice_str == ("Paper"):
        print("Draw")

    if user_choice == ("Paper") and computer_choice_str == ("Scissors"):
        print("The computer wins! :(")

    if user_choice == ("Scissors") and computer_choice_str == ("Rock"):
        print("The computer wins! :(")

    if user_choice == ("Scissors") and computer_choice_str == ("Paper"):
        print("The user wins! :)")

    if user_choice == ("Scissors") and computer_choice_str == ("Scissors"):
        print("Draw")
