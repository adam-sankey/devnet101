#import the requests library
import requests

#read input from the user and set it to the 'message' variable
message = input("Message: ")

#set the 'url' variable to the webex url
url = "https://api.ciscospark.com/v1/messages"

#define body and header data
payload="{\r\n  \"roomId\" : \"Y2lzY29zcGFyazovL3VzL1JPT00vNzY2MzkyYTAtYTg3MS0xMWViLTkxYTItYWY4MWE5NjEzMDdj\",\r\n  \"text\" : \"" + message + "\"\r\n}"
headers = {
  'Authorization': 'Bearer XXXXX',
  'Content-Type': 'application/json'
}

#make the API call and save the response into the 'response' variable
response = requests.request("POST", url, headers=headers, data=payload)

#evaluate if the response was successful
if response.status_code == 200:
    print("Success!")
else:
    print("Message failed. Code: ", response.status_code)
    print(response.text)