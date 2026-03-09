from main import iss_retirement_check, iss_location

def test_iss_deorbit():
    year = 2050
    result = iss_retirement_check(year)
    assert result == {
        "location": "South Pacific Ocean",
        "note": "The ISS has been deorbited and this is its landing site."
    }

    
# def test_retirement_not_triggered():

#     assert {
#             "latitude": latitude,
#             "longitude": longitude,
#             "location": location
#         }