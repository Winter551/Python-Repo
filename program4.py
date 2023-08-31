names = []
code = []

with open ("data.csv","r") as countries_csv:
    lines = countries_csv.readlines()

    for i in lines:
        new_list = i.split(",")
        names.append(new_list[0])
        code.append(new_list[1])

    for i in range(len(names)):
        print("-----------")
        print("Name: " + names[i])
        print("Code: " + code[i])