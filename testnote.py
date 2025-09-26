from datetime import datetime, timezone

def iss_retirement_check():
    year = datetime.now(timezone.utc).year
    print(year)
    if year >= 2031:
        return {
            "location": "South Pacific Ocean",
            "note": "The ISS has been deorbited and this is its landing site."
        }
    return None

iss_retirement_check()