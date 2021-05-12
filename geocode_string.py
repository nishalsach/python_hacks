# Use this to get a geocode for a string location - gives you latitude and longitude
from geopy.geocoders import Nominatim

# Define the function
def get_location(location_string):
    
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(location_string, timeout = 50)
    
    return location
  
# Create columns with call
df['location_geocoded'] = df['location_string'].apply(lambda x: get_location(x))
df.head()

