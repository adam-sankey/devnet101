#import modules
import json
import requests

#set URL as a variable
url = "https://api.ciscospark.com/v1/rooms"

#define header and body of API request
payload={}
headers = {
  'Authorization': 'Bearer XXXXX'
}

#execute API call and save response to 'response' variable
response = requests.request("GET", url, headers=headers, data=payload)

if response.status_code == 200:

    #load response in json format and prepare for parsing
    roomList = response.text
    roomList = json.loads(roomList)
    roomList = roomList["items"]

    #list room name and IDs
    for x in roomList:
        print("Room Name = ", x["title"])
        print("Room ID = ", x["id"], "\n")

else:
    print("Error code: ", response.status_code)
    print(response.text)
