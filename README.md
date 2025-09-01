ISS Location Tracker

A FastAPI web application that tracks the **International Space Station's (ISS)** current position and tells you which country or ocean it is flying over — using real geospatial data.

---

## Table of Contents

- [About](#about)
- [Features](#features)
- [API Endpoints](#api-endpoints)
- [Example Response](#example-response)
- [Getting Started](#getting-started)
- [Tech Stack](#tech-stack)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

---

## About

This project fetches live ISS latitude and longitude from a public API, uses detailed country and ocean boundaries (Natural Earth datasets), and efficiently determines whether the ISS is over land or water. It provides this data via REST API endpoints in real-time.

**Why this project?**  
Because I’m curious about space and coding, and I wanted to combine the two.

---

FEATURES

- Fetch live ISS coordinates from a public API  
- Use geospatial data with GeoPandas and Shapely  
- Determine whether the ISS is over land or ocean  
- REST API endpoints returning JSON  
- Efficient handling of large geodata (polygon simplification, indexing)  
- Securely handle environment variables for external APIs  

---

## API Endpoints

### `GET /iss-location`

Returns the current ISS position along with the country or ocean it is above.

---

## Example Response

```json
[
  { "name": "Canada" },
  { "name": "North Atlantic Ocean" }
]
```
## Getting Started

### Installation


### Fork the repository on GitHub

### Clone the repository
git clone https://github.com/YOUR-USERNAME/isstracker
cd isstracker


### (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

### Create a .env file (recommended)
echo "URL_ISS=https://api.open-notify.org/iss-now.json" > .env
or manually copy the URL into the .env file

### Install dependencies
pip install -r requirements.txt

### Start FastAPI server in development mode with auto-reload
uvicorn main:app --reload --host 0.0.0.0 --port 8000

### Tech Stack

- **Language:** Python 3.8+  
- **Framework:** FastAPI  
- **Server:** Uvicorn (ASGI)  
- **Geospatial:** GeoPandas, Shapely  
- **API Requests:** Requests  
- **Environment Variables:** python-dotenv  

---

## Contributing

Feel free to open issues or submit pull requests.  
Contact me at **bastugugur85@gmail.com** for bug reports, suggestions, or collaboration.

---

## License

This project is licensed under the **MIT License** — Uğur Baştuğ

## Additional Notes

- The ISS is scheduled to be deorbited and landed in the ocean around 2030. I plan to hardcode the landing site in the app at that time. The project may be updated again if revisited in the future.
