rank = []
firstn = []
lastn = []


employees = {"Joe":"Doctor","Sue":"Teacher","Alex":"Nerd","Beck":"Hacker"}


with open("gender_names.csv","r") as names_csv:
    lines = names_csv.readlines()

    for i in lines:
        new_list = i.split(",")
        rank.append(new_list[0])
        firstn.append(new_list[1])
        lastn.append(new_list[2])
    
    for i in range(len(firstn)):
        print("-----------")
        print("Rank: " + rank[i])
        print("Girl Name: " + firstn[i])
        print("Boy Name: " + lastn[i])

for k,v in employees.items():
    print("--------------")
    print("Name: " + k)
    print("Job: " + v)