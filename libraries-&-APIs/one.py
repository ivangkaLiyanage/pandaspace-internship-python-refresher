# Use the `requests` library to fetch data from a public API and display it.
import requests

req = requests.get('https://api.github.com/users/ivangkaLiyanage')
print(req)
# print(req.content)

# extracting data in json format
data = req.json()
 
 
# extracting data
login = data['login']
followers = data['followers']
createdDate = data['created_at']
twitterID = data['twitter_username']
name = data['name']


# printing the output
print("Login: %s\nFollowers: %s\ntwitterID: %s\nCreated: %s\nName: %s\n"
    %(login, followers,twitterID, createdDate,name))