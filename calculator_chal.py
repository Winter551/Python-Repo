x = input("Pick a number: ")
y = input("Pick another number: ")
z = input("Pick an operator: ")

if z == ("*"):
    print(int(x) * int(y))
if z == ("/"):
    print(int(x) / int(y))
if z == ("+"):
    print(int(x) + int(y))
if z == ("-"):
    print(int(x) - int(y))