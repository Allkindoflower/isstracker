import requests


api = 'http://api.auroras.live/v1/?type=locations'


response = requests.get(api)

data = response.json()

for key, aurora in data.items():
    if key == 'message':
        continue
    else:
        print(f'Aurora name: {aurora['name']}||Country: {aurora['country']}'.strip())


