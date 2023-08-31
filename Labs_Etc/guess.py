import requests
import random

r = requests.get("http://172.25.0.20")

random_get = random.randint(1,1000)

while True:
    response = requests.get("http://172.25.0.20?guess=" + str(random_get))
    current_page_text = response.text
    if "wrong!" not in current_page_text:
        print(response.text)
        print("http://172.25.0.20?guess=" + str(random_get))