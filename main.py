from fastapi import FastAPI, HTTPException
import requests
import os
import geopandas as gpd
from shapely.geometry import Point
import dotenv
from fastapi.staticfiles import StaticFiles


dotenv.load_dotenv()

app = FastAPI()

#app.mount("/", StaticFiles(directory="static", html=True), name="static")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(BASE_DIR, 'data')

lands_path = os.path.join(data_dir, 'countries.geojson')
oceans_path = os.path.join(data_dir, 'oceans.geojson')

lands = gpd.read_file(lands_path)
oceans = gpd.read_file(oceans_path)

@app.get("/iss-location")
async def iss_location():
    url_iss = os.getenv('url_iss')
    if not url_iss:
        raise HTTPException(status_code=500, detail="ISS API URL not configured")
    try:
        response = requests.get(url_iss, timeout=5)
        response.raise_for_status()
        data = response.json()
        longitude = float(data['iss_position']['longitude'])
        latitude = float(data['iss_position']['latitude'])
        point = Point(longitude, latitude)

        possible_ocean_idxs = list(oceans.sindex.intersection(point.bounds))
        possible_oceans = oceans.iloc[possible_ocean_idxs]
        ocean_match = possible_oceans[possible_oceans.contains(point)]

        possible_land_idxs = list(lands.sindex.intersection(point.bounds))
        possible_lands = lands.iloc[possible_land_idxs]
        lands_match = possible_lands[possible_lands.contains(point)]

        location = None
        if not ocean_match.empty:
            location = ocean_match.iloc[0]['NAME']
        elif not lands_match.empty:
            location = lands_match.iloc[0]['name']
        else:
            location = "Unknown area"

        return {
            "latitude": latitude,
            "longitude": longitude,
            "location": location
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
