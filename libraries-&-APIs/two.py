import requests
API_KEY = "4ecbe586009948028c9501383d871cff"

# url = "https://api.weatherbit.io/v2.0/current?lat=35.7796&lon=-78.6382&key=API_KEY&include=minutely"


# Make the GET request to the API
# url = f"https://api.weatherbit.io/v2.0/current?lat=35.7796&lon=-78.6382&key={API_KEY}&include=minutely"
url = f"https://api.weatherbit.io/v2.0/current?&city=Burwood&country=Australia&key={API_KEY}&include=minutely"


response = requests.get(url)

# Print the status code of the response
print(response.status_code)

# Print the content of the response (formatted as JSON)
data = response.json()

timezone = data['timezone']

print('Timezone: %s\n'
      %(timezone))


