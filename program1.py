import random

x = input("Pick a number between 1 and 100: ")

y = random.randint(1,100)

print ("You picked " + x + " and the number " + str(y) + " was generated")

print(f"You picked {x} and the number generated was {y}".format(x,y))


if int(x) < y:
    print ("Too low :(")
if int(x) > y:
    print ("Too high :(")
if int(x) == y:
    print ("Correct! :)")
    