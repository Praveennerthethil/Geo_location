from geopy.geocoders import Nominatim


loc = Nominatim(user_agent="GetLoc")
getLoc = loc.geocode("...Location_name...")
print("Latitude = ", getLoc.latitude,"\n")
print("Longitude = ", getLoc.longitude)