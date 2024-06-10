from geopy.geocoders import Nominatim

def get_location_info(address):
    loc = Nominatim(user_agent="GetLoc")
    location = loc.geocode(address)
    return {
        'address': location.address,
        'latitude': location.latitude,
        'longitude': location.longitude
    }
