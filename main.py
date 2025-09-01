from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
import requests
import os
import geopandas as gpd
from shapely.geometry import Point
import dotenv
from datetime import datetime, timezone


dotenv.load_dotenv()

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/", StaticFiles(directory="static", html=True), name="static")

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
    # --- Forward-looking ISS retirement logic ---
    # At the end of 2030, the ISS will be deorbited.
    # The API will automatically return the landing site and a note
    # instead of live coordinates, so no manual updates are required.
    ISS_RETIREMENT_YEAR = 2031
    LANDING_SITE = "South Pacific Ocean"
    NOTE = "The ISS has been deorbited and this is its landing site."

    current_year = datetime.now(timezone.utc).year
    if current_year >= ISS_RETIREMENT_YEAR:
        return {
            "latitude": None,
            "longitude": None,
            "location": LANDING_SITE,
            "note": NOTE
        }
    try:
        response = requests.get(url_iss, timeout=10)
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
