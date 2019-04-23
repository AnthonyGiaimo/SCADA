# importing the requests library
import requests

# api-endpoint
URL = "https://tony-giaimo.us/coffee.php"
token = "DogKt8rm6oT5txK6nj6zTMbJV4Wn94fI"

# user given here
request = "oof"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'request': request, 'auth': token}

# sending post request and saving the response as response object
r = requests.get(url=URL, params=PARAMS)

# extracting data in json format

print(r.text)
