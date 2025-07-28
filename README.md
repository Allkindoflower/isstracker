ISS Location Tracker
A FastAPI web application that tracks the International Space Station's current position and tells you which country or ocean it's flying over — using real geospatial data.
Feel free to contact me if you find bugs or want to contribute

What it does

Fetches live ISS latitude and longitude from a public API
Uses detailed country and ocean boundaries (Natural Earth datasets)
Efficiently determines whether the ISS is over land or water through REST API endpoints
Provides real-time location data via JSON responses


Why this project?
Because I’m curious about space. And code. And what happens when you mix the two.

Features:
Geospatial data and shapefiles (converted to GeoJSON for speed)
Spatial queries using GeoPandas and Shapely
Handling external APIs and environment variables securely
Optimizing slow geodata processing by simplifying polygons and indexing
Building responsive web APIs with FastAPI


API Endpoints

GET /iss-location - Returns current ISS position with country/ocean information


How to use:

Clone the repo
git clone <repository-url>
cd isstracker

Run the conversion script once to create GeoJSON files:
python convert_to_json.py

Set your ISS API URL in a .env file:
URL_ISS=https://api.open-notify.org/iss-now.json

Install dependencies:
pip install -r requirements.txt

Run the FastAPI server:
uvicorn main:app --reload

Access the API at http://localhost:8000 or visit http://localhost:8000/docs for interactive API documentation


Example Response:

json{
  "iss_position": {
    "latitude": 45.2841,
    "longitude": -75.6762
  },
  "location": {
    "type": "country",
    "name": "Canada"
  }
}

Requirements

Python 3.8+
FastAPI
Uvicorn (ASGI server)
GeoPandas
Shapely
Requests
Python-dotenv

Install all packages with:
pip install fastapi uvicorn geopandas shapely requests python-dotenv
Or use the requirements.txt file:
pip install -r requirements.txt

Development
Run in development mode with auto-reload:
uvicorn main:app --reload --host 0.0.0.0 --port 8000

Possible future improvements

Add GUI/web interface with interactive map
Cache recent locations to reduce redundant checks
More detailed region info (e.g., states, seas)
Use a faster spatial database (like PostGIS) for larger scale
Add WebSocket support for real-time updates
Implement rate limiting and API authentication


License
MIT License — It's yours, baby. Use it however you like!
