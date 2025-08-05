# ISS Location Tracker

A FastAPI web application that tracks the International Space Station's current position and tells you which country or ocean it's flying over — using real geospatial data.

Feel free to contact me at bastugugur85@gmail.com if you find bugs or want to contribute.

## What It Does

- Fetches live ISS latitude and longitude from a public API
- Uses detailed country and ocean boundaries (Natural Earth datasets)
- Efficiently determines whether the ISS is over land or water through REST API endpoints
- Provides real-time location data via JSON responses

## Why This Project?

Because I’m curious about space. And code. And what happens when you mix the two.

## Features

- Geospatial data and shapefiles (converted to GeoJSON for speed)
- Spatial queries using GeoPandas and Shapely
- Handling external APIs and environment variables securely
- Optimizing slow geodata processing by simplifying polygons and indexing
- Building responsive web APIs with FastAPI

## API Endpoints

**GET** `/iss-location`

Returns current ISS position with country/ocean information in JSON format.

## How to Use

```bash
fork my repo
'git clone https://github.com/YOUR-USERNAME/isstracker' using git bash
cd /path/to/isstracker

# Run conversion script once to create GeoJSON files
python convert_to_json.py

# Create a .env file with your ISS API URL
echo "URL_ISS=https://api.open-notify.org/iss-now.json" > .env

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
uvicorn main:app --reload
```

Access the API at [http://localhost:8000](http://localhost:8000/docs)


Example response:

{
  "name": "Canada"
}

## Requirements
Python 3.8+
FastAPI
Uvicorn (ASGI server)
GeoPandas
Shapely
Requests
Python-dotenv

Install packages via:
pip install -r requirements.txt

Run in development mode with auto-reload:
uvicorn main:app --reload --host 0.0.0.0 --port 8000

Possible Future Improvements:

-Add GUI/web interface with interactive map<br>
-Cache recent locations to reduce redundant checks<br>
-Provide more detailed region info (e.g., states, seas)<br>
-Use a faster spatial database (like PostGIS) for larger scale<br>
-Add WebSocket support for real-time updates<br>
-Implement rate limiting and API authentication<br>

License
MIT License — It’s yours, baby. Use it however you like!

