#Racecar simulator
import random
import time

car_list = {"Audi R8":205, "Nissan GTR":198, "McLaren P1":217, "Lamborghini Hurican Performante":201, "Chevrolet Corvette C8":194}
random_racers = ["Walace Winnin", "Sofi 'Sop' Lin", "Rafael Racist", "Carson Cars", "Martin Motorist", "Sam 'Sam' Harrold"]

print()
print()
print("Welcome new driver to the [2023 VIRTUAL PYTHON CUP (VPC)]")
time.sleep(2)
print("You will first PICK A CAR, then you will PICK YOUR SPEED you will use throughout the race")
time.sleep(3)
print("You have A FEW CARS TO PICK FROM, each one with a different engine and therefore a DIFFERENT TOP SPEED")
time.sleep(3)
print()
print(f"The CARS YOU CAN PICK FROM are:")
for car, speed in car_list.items():
    print(f"[ {car}, with a top speed of {speed} MPH ]")
    time.sleep(0.5)

print()

for car, speed in car_list.items():

    user_select_car = input("WHICH CAR would you like to pick?: ")
    print()

    if user_select_car not in car_list:
        print("This is NOT A VALID CAR, please TRY AGAIN")
        print()
    else:
        user_car = user_select_car
        break

user_speed = car_list[user_car]

time.sleep(1)
print("Alright, YOU HAVE CHOSEN YOUR CAR...")
time.sleep(2)
print("LET THE RACE BEGIN!")
time.sleep(2)
print()


leg1 = int(input((f"CHOOSE YOUR SPEED for the [1ST] leg of the race [0 - {user_speed} MPH]: ")))
time.sleep(2)

racing = True
while racing == True:

    comp_speed = random.randint(100, 230)
    speed_crash = random.randint(190, 220)

    if leg1 > user_speed:
        print("You PUSHED YOUR ENGINE TOO FAR")
        print("You are OUT OF THE RACE")
        print()
        lost = True

    if leg1 == speed_crash:
        print("You CRASHED!")
        print("You are OUT OF THE RACE")
        print()
        lost = True

    if comp_speed > leg1:
        print("You were BEATEN IN LEG 1 of the race")
        print()
        lost = False
        lost1 = True
    else:
        print("You WON THE 1ST LEG of the race")
        print()
        lost = False
        lost1 = False
    racing = False

if lost == True:
    print("I am so sorry but you have been DISQUALIFIED from the 2023 VIRTUAL PYTHON CUP (VPC)")
    print("See you next year!")
    exit()
else:
    print()

leg2 = int(input((f"CHOOSE YOUR SPEED for the [2ND] leg of the race [0 - {user_speed} MPH]: ")))
time.sleep(2)

racing = True
while racing == True:

    comp_speed = random.randint(100, 230)
    speed_crash = random.randint(190, 210)

    if leg2 > user_speed:
        print("You PUSHED YOUR ENGINE TOO FAR")
        print("You are OUT OF THE RACE")
        print()
        lost = True

    if leg2 == speed_crash:
        print("You CRASHED!")
        print("You are OUT OF THE RACE")
        print()
        lost = True

    if comp_speed > leg2:
        print("You were BEATEN IN LEG 2 of the race")
        print()
        lost = False
        lost2 = True
    else:
        print("You WON THE 2ND LEG of the race")
        print()
        lost = False
        lost2 = False
    racing = False

if lost == True:
    print("I am so sorry but you have been DISQUALIFIED from the 2023 VIRTUAL PYTHON CUP (VPC)")
    print("See you next year!")
    exit()
else:
    print()

leg3 = int(input((f"CHOOSE YOUR SPEED for the [3RD] leg of the race [0 - {user_speed} MPH]: ")))
time.sleep(2)

racing = True
while racing == True:

    comp_speed = random.randint(100, 230)
    speed_crash = random.randint(190, 210)

    if leg3 > user_speed:
        print("You PUSHED YOUR ENGINE TOO FAR")
        print("You are OUT OF THE RACE")
        print()
        lost = True

    if leg3 == speed_crash:
        print("You CRASHED!")
        print("You are OUT OF THE RACE")
        print()
        lost = True

    if comp_speed > leg3:
        print("You were BEATEN IN LEG 3 of the race")
        print()
        lost3 = True
        lost = False
    else:
        print("You WON THE 3ND LEG of the race")
        print()
        lost3 = False
        lost = False
    racing = False

if lost == True:
    print("I am so sorry but you have been DISQUALIFIED from the 2023 VIRTUAL PYTHON CUP (VPC)")
    print("See you next year!")
    exit()
else:
    print()

random_winner = random.randint(0, 5)
time.sleep(1)
print("The race has CONCLUDED!")
print()
print("The RESULTS ARE IN:")
time.sleep(2)
if lost1 == True:
    print(f"The winner of the [1ST] LEG OF THE RACE is: [{random_racers[random_winner]}]")
    time.sleep(2)
else:
    print(f"The winner of the [1ST] LEG OF THE RACE is: [YOU]")
    time.sleep(2)
if lost2 == True:
    print(f"The winner of the [2ND] LEG OF THE RACE is: [{random_racers[random_winner]}]")
    time.sleep(2)
else:
    print(f"The winner of the [2ND] LEG OF THE RACE is: [YOU]")
    time.sleep(2)
if lost3 == True:
    print(f"The winner of the [3RD] LEG OF THE RACE is: [{random_racers[random_winner]}]")
    time.sleep(2)
    print()
else:
    print(f"The winner of the [3RD] LEG OF THE RACE is: [YOU]")
    time.sleep(2)
    print()

print("So the overall winner of the [2023 VIRTUAL PYTHON CUP (VPC)] is...")
time.sleep(2)
print("...")
time.sleep(3)

if lost1 and lost2 == True:
    print(f"[{random_racers[random_winner]}]")
    print()
elif lost2 and lost3 == True:
    print(f"[{random_racers[random_winner]}]")
    print()
elif lost1 and lost3 == True:
    print(f"[{random_racers[random_winner]}]")
    print()
else:
    print("[YOU]")
    print()

time.sleep(2)
print("Thanks for participating in the [2023 VIRTUAL PYTHON CUP (VPC)]")
print("See you next year!")
print()
time.sleep(2)