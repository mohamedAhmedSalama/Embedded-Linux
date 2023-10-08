# get automatically activity & public url
import requests
from time import sleep
url = requests.get("https://api.ipify.org/?format=json")
print("your IP is: ",url.text)
while True:
    url = requests.get("https://www.boredapi.com/api/activity")
    print(url.json()['activity'])
    sleep(2)








