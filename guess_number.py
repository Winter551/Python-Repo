import random

random_number = random.randint(1,100)

user_number = int(input("Pick a number between 1 and 100: "))

if user_number > random_number:
    print("Too high :(")
elif user_number < random_number:
    print("Too low :(")
else:
    print("Correct! :)")