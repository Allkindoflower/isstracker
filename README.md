ISS Location Tracker — Countries & Oceans Edition
A simple Python script that tracks the International Space Station’s current position and tells you which country or ocean it’s flying over — using real geospatial data.

What it does
Fetches live ISS latitude and longitude from a public API

Uses detailed country and ocean boundaries (Natural Earth datasets)

Efficiently determines whether the ISS is over land or water, and prints the name

Runs continuously, updating every 10 seconds with a clear console display

Why this project?
I wanted to challenge myself by working with:

Geospatial data and shapefiles (converted to GeoJSON for speed)

Spatial queries using GeoPandas and Shapely

Handling external APIs and environment variables securely

Optimizing slow geodata processing by simplifying polygons and indexing

How to use
Clone the repo

Download the required Natural Earth shapefiles (ne_10m_admin_0_countries.shp and World_Seas_IHO_v3.shp) into the data folder

Run the conversion script once to create GeoJSON files:

python convert_to_geojson.py
Set your ISS API URL in a .env file:

url_iss=https://api.open-notify.org/iss-now.json

Run the tracker:

python iss_tracker.py


Notes
The ocean shapefile is quite large and can take a few minutes to process when converting. This is a one-time step.

Geometries are simplified to speed up location checks; this might slightly reduce accuracy over complex coastlines.

The tracker refreshes every 10 seconds — adjust the interval in the script if needed.

Requirements
Python 3.8+

Packages: geopandas, shapely, requests, python-dotenv

Install packages with:


pip install geopandas shapely requests python-dotenv

Future improvements
Add GUI/web interface

Cache recent locations to reduce redundant checks

More detailed region info (e.g., states, seas)

Use a faster spatial database (like PostGIS) for larger scale

License
MIT License — feel free to use and modify!




