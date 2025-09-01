ISS Location Tracker

A FastAPI web application that tracks the International Space Station's (ISS) current position and tells you which country or ocean it is flying over --- using real geospatial data.

TABLE OF CONTENTS

1. About

2. Features

3. API Endpoints

4. Example Response

5. Getting Started

6. Tech Stack

7. Future Improvements

8. Contributing

9. License

ABOUT

This project fetches live ISS latitude and longitude from a public API, uses detailed country and ocean boundaries (Natural Earth datasets), and efficiently determines whether the ISS is over land or water. It provides this data via REST API endpoints in real-time.

Why this project?

Because I'm curious about space and coding, and I wanted to combine the two.

FEATURES

- Fetch live ISS coordinates from a public API

- Use geospatial data with GeoPandas and Shapely

- Determine whether the ISS is over land or ocean

- REST API endpoints returning JSON

- Efficient handling of large geodata (polygon simplification, indexing)

- Securely handle environment variables for external APIs

API ENDPOINTS

GET /iss-location

Returns the current ISS position along with the country or ocean it is above.

EXAMPLE RESPONSES

{

  "name": "Canada"

},

{

  "name": "North Atlantic Ocean"

}

GETTING STARTED

Prerequisites:

- Python 3.8+

- Git

Installation:

1. Clone the repository:

   git clone https://github.com/YOUR-USERNAME/isstracker

   cd isstracker

2. Create a .env file (optional, recommended):

   echo "URL_ISS=https://api.open-notify.org/iss-now.json" > .env

   or manually copy the URL into the .env file

3. Install dependencies:

   pip install -r requirements.txt

Running the Server:

Start FastAPI server in development mode with auto-reload:

   uvicorn main:app --reload --host 0.0.0.0 --port 8000

Access the API documentation at: http://localhost:8000/docs

TECH STACK

- Language: Python 3.8+

- Framework: FastAPI

- Server: Uvicorn (ASGI)

- Geospatial: GeoPandas, Shapely

- API Requests: Requests

- Environment Variables: python-dotenv

FUTURE IMPROVEMENTS

- Add a GUI/web interface with an interactive map

- Cache recent locations to reduce redundant processing

- Use a faster spatial database (e.g., PostGIS) for scalability

- Add WebSocket support for real-time updates

- Implement rate limiting and API authentication

CONTRIBUTING

Feel free to open issues or submit pull requests.

Contact: bastugugur85@gmail.com for bug reports, suggestions, or collaboration.

LICENSE

MIT License --- Uğur Baştuğ