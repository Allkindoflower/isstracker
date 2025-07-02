import requests
import time
import os
import geopandas as geo
import dotenv
from shapely.geometry import Point

dotenv.load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(BASE_DIR, 'data')

lands_path = os.path.join(data_dir, 'countries.geojson')
oceans_path = os.path.join(data_dir, 'oceans.geojson')

lands = geo.read_file(lands_path)
oceans = geo.read_file(oceans_path)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_iss_location():  
    url_iss = os.getenv('url_iss')
    response_iss = requests.get(url_iss, timeout=5)
    data_iss = response_iss.json()
    longitude = data_iss['iss_position']['longitude']
    latitude = data_iss['iss_position']['latitude']
    return float(latitude), float(longitude)

while True: 
    try:
        latitude, longitude = get_iss_location()
        point = Point(longitude, latitude)
        #Code below quickens the search by eliminating far off points
        possible_ocean_idxs = list(oceans.sindex.intersection(point.bounds))
        possible_oceans = oceans.iloc[possible_ocean_idxs]
        ocean_match = possible_oceans[possible_oceans.contains(point)]

        possible_land_idxs = list(lands.sindex.intersection(point.bounds))
        possible_lands = lands.iloc[possible_land_idxs]
        lands_match = possible_lands[possible_lands.contains(point)]
        #Code above quickens the search by eliminating far off points
        print(f'Lat: {latitude}, Lon: {longitude}')
        if not ocean_match.empty:
            print(ocean_match.iloc[0]['NAME'])
        elif not lands_match.empty:
            print(lands_match.iloc[0]['ADMIN'])
        else:
            print('ISS over unknown area')
 
    except Exception as e:
        print(f'Error: {e}')
    time.sleep(10)
    clear_terminal()
    

    
