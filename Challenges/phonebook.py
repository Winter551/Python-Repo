phonebook = {}
phonebook_del = []

print("--------------")
print("Welcome to your personal Phonebook!")
print("If you would like more info on what I can do type [Info]")
while True:
    action = input("What action would you like to perform? ")
    print("--------------")

    if action == ("Add"):
        num_add = input("What Phone Number would you like to add to your phonebook? ")
        num_nodash = num_add.replace("-","")
        name_add = input("What name would you like to associate with this number? ")
        print("--------------")
        phonebook.update({name_add:num_add})
    if action == ("View"):
        if phonebook == ({}):
            print("There is nothing in your phonebook")
            print("--------------")
        else:
            print("Your current phonebook consists of the following names and numbers: ")
            print(phonebook)
            print("--------------")
    if action == ("Search"):
        search = input("What Name or Number would you like to search for? ")
        print("--------------")
        found = False
        for key, value in phonebook.items():
            if search in key or search == value:
                print(f"{key} - {value}")
                print("--------------")
                found = True
        if found == False:
            print("Your string did not match any Name or Number in this phonebook.")
            print("--------------")
    if action == ("Delete"):
        print("Which Name and Number pair would you like to delete?")
        print("(You only have to enter one of the pair for both to be deleted)")
        phone_delete = input("> ")
        print("--------------")
        for k, v in phonebook.items():
            if phone_delete in k or phone_delete == v:
                phonebook_del.append(k)
        for k in phonebook_del:
            del phonebook[k]