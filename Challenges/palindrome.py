print("This is a Palindrome checker")


while True:
    print("What string would you like to check for a Palindrome?")
    user_string = input("> ")
    print("--------------")

    rev_string = user_string[::-1]

    if rev_string.casefold() == user_string.casefold():
        print(f"Your string was [{user_string}]")
        print("This string is a Palindrome!")
        print("--------------")
    else:
        print(f"Your string was [{user_string}]")
        print("This string is not a Palindrome :(")
        print("--------------")