
def ask_for_input():
    number_picked = input("Pick a number: ")
    return number_picked

def echo_user_input(x):
    print(x)

def add_two_numbers(x,y):
    z = int(x) + int(y)
    print(z)

def multiply_inputs(x,y,z):
    m = int(x) * int(y) * int(z)
    return m

def determine_largest(x,y):
    if int(x) > int(y):
        print(x)
    else:
        print (y)


a = ask_for_input()
b = ask_for_input()
c = ask_for_input()

add_two_numbers(a,b)

multiply_inputs(a,b,c)

determine_largest(a,b)