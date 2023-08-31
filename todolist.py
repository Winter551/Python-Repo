tasks = []
done_tasks = []

print("Welcome to your To-Do list, what action would you like to perform? (Add/Check/View/Exit)")

while True:

    action = input("Pick an action: ")

    if action == ("Add"):
        print("--------------")
        todo_add = input("What would you like to add to your Todo list? ")
        print("--------------")
        tasks.append(todo_add)
        print(todo_add + " was added to your Todo list.")
        print("--------------")
    elif action == ("View"):
        if tasks == ([]):
            print("--------------")
            print("There is nothing on your Todo list.")
            print("--------------")
        else:
            print("--------------")
            print("This is what is on your current Todo list: ")
            print(tasks)
            print("--------------")
    elif action == ("Check"):
        if tasks == ([]):
            print("There is nothing on your Todo list.")
            print("--------------")
        else:
            print("--------------")
            print("Your current To-Dos are: " + str(tasks))
            todo_check = input("What task would you like to check off? ")
            print("--------------")
            if todo_check == (tasks[0]) or (tasks[1]) or (tasks[2]) or (tasks[3]) or (tasks[4]):
                done_tasks.append(todo_check)
                print(todo_check + " has been checked off of your To-Do list. Congrats!")
                tasks[tasks.index(todo_check)] += " (Checked)"
                print("--------------")
            else:
                print("--------------")
                print("This is not a valid task. Please retry.")
                print("--------------")
    elif action == ("Exit"):
        print("--------------")
        print("Goodbye!")
        break
    else:
        print("--------------")
        print("That is not a valid input, please retry.")
        print("--------------")