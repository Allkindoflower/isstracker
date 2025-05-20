import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def getIssLocation():  
    url_iss = os.getenv('url_iss')
    response_iss = requests.get(url_iss)
    data_iss = response_iss.json()
    latitude = data_iss['iss_position']['latitude']
    longitude = data_iss['iss_position']['longitude']
    return latitude, longitude
         

def findCountry(latitude, longitude):
    key_reversegeo = os.getenv('key_reversegeo')
    url_reversegeo = f'https://us1.locationiq.com/v1/reverse?key={key_reversegeo}&lat={latitude}&lon={longitude}&format=json&'
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
    time.sleep(2)
    clear_terminal()
    
    
