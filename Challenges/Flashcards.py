#Studying flashcards maker thing

import random

study_words = {}

running = True

print("Welcome to Sam's Build-Your-Own-Flashcards (BYOF)")
print("")

while running is True:

  print("What action would you like to select? [Type: \"Help\" for help] ")
  user_action = input("> ")
  print()

  #Adding user's word and meaning to the dict
  if user_action == ("Add"):
    user_add_words = input("What term would you like to add your study list?: ")
    user_add_meaning = input("What meaning would you like to assign to your term?: ")
    study_words[user_add_words] = (user_add_meaning)
    print(f"[{user_add_words}] and its meaning [{user_add_meaning}] have been added to your flashcards list.")
    print()

  #Lets a user study their current flashcards
  #Ngl used ChatGPT for some things in here cuz im dumb
  if user_action == "Study":
    used_flashcards = []

    #For everything in study_words
    for _i in study_words:
      study_cards_num = len(study_words)

      #Checking if the dict has anything in it
      if study_cards_num == 0:
        print("There is nothing in your flashcard set, please add a set before attempting to study")
        print()
      #Checks to make sure it doesn't repeat a previously printed flashcard
      else:
        while True:
          random_flashcard = random.randint(0, study_cards_num - 1)
          if random_flashcard not in used_flashcards:
            used_flashcards.append(random_flashcard)
            break

        #Randomly generates a word and meaning from the dict
        random_word, random_meaning = list(study_words.items())[random_flashcard]

        #Asks user for the meaning to the word
        print(f"Random Flashcard #{random_flashcard + 1}:")
        print(f"Word: [{random_word}]")
        user_guess = input("Enter your guess for the word: ")
        print()

        #Telling the user if they are correct or dumb
        if user_guess == random_meaning:
          print("[Correct!]")
        else:
          print("[Incorrect!] The correct meaning was:")
          print(f"[{random_meaning}]")
        print()
        

  #Lets you view all of your flashcards
  if user_action == ("View"):
    print("Your current study list consists of the words and meanings:")
    for word, meaning in study_words.items():
      print(f"[{word}] - [{meaning}]")
    print()

  #Lets the user see every command they can do
  if user_action == ("Help"):
    available_actions = ["[Add] - Adds a flashcard set", 
                         "[Study] - Lets you study your existing flashcards", 
                         "[View] - Lets you view your existing flashcards", 
                         "[Help] - Lets you see the current commands available"
                        ]
    print("The current available actions are: ")
    print()
    for i in available_actions:
      print(i)
    print()

#I prob wont use this cuz its temporary but yk whatever
#I could add permability to this but eh
#I like the pretty colors in Github
#I've also realized that most of my code is just if statments but whatelse will i do huh
