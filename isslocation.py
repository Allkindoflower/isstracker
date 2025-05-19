import requests
import time
import os


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def getIssLocation():   
    url_iss = 'http://api.open-notify.org/iss-now.json'
    response_iss = requests.get(url_iss)
    data_iss = response_iss.json()
    latitude = data_iss['iss_position']['latitude']
    longitude = data_iss['iss_position']['longitude']
    return latitude, longitude
         

def findCountry(latitude, longitude):
    url_reversegeo = f'https://us1.locationiq.com/v1/reverse?key=pk.4455fb17e19dec3d3a5bd7e45ef70c58&lat={latitude}&lon={longitude}&format=json&'
    response_geo = requests.get(url_reversegeo)
    data_geo = response_geo.json()
    return data_geo

while True:
    
    try:
        latitude, longitude = getIssLocation()
        data_geo = findCountry(latitude, longitude)   
        if 'address' in data_geo:
            if 'country' in data_geo['address']:
                print(data_geo['address']['country'])
        else:
            print('Ocean/Sea')
    except (KeyError, ValueError, TypeError, requests.exceptions.RequestException):
        print('Cannot reach the location information.')
    time.sleep(20)
    clear_terminal()
    
    
