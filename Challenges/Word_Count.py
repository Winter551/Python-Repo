words = []


while True:
    print("----------------")
    print("Paste text input: ")
    user_string = input("> ")
    print("----------------")
    user_freq = input("What word would you like to find the frequency of? ")

    words = user_string.split()

    if user_freq in words:
        word_choice = int(words.index(user_freq))
        word_freq = words.count(words[word_choice])
        print(user_freq + " frequency : " + str(word_freq))
    else:
        print("----------------")
        print("This is not a valid word in the provided string, please try again.")