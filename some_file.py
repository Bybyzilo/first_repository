# print('My first repository!')

# print('New commit for test')
import requests
import pprint


api_url = 'http://api.open-notify.org/iss-now.json'

response = requests.get(api_url)

if response.status_code == 200:
    pprint.pprint(response.text)
else:
    pprint.pprint(response.status_code)
