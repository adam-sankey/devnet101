#import the requests library
import requests

#set the 'url' variable to the webex url
url = "https://api.ciscospark.com/v1/messages"

#define body and header data
payload="{\r\n  \"roomId\" : \"Y2lzY29zcGFyazovL3VzL1JPT00vNzY2MzkyYTAtYTg3MS0xMWViLTkxYTItYWY4MWE5NjEzMDdj\",\r\n  \"text\" : \"hi from Postman\"\r\n}"
headers = {
  'Authorization': 'Bearer XXXXX',
  'Content-Type': 'application/json'
}

#make the API call and save the response into the 'response' variable
response = requests.request("POST", url, headers=headers, data=payload)

#print the raw response data
print(response.text)
