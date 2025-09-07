from main import iss_retirement_check

def test_iss_deorbit():
    result = iss_retirement_check(2031)
    assert result == {
        "location": "South Pacific Ocean",
        "note": "The ISS has been deorbited and this is its landing site."
    }

def test_retirement_not_triggered():
    result = iss_retirement_check(2025)
    assert result is None