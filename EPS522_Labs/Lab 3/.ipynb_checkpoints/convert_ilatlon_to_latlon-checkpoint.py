# Define a function that will convert values from 0 to 180 into latitude and values from 0 to 360 to longitude
def convert_ilatlon_to_latlon(latitude_number, longitude_number):
    # Check if latitude number is within range [0, 180]
    if 0 <= latitude_number <= 180:
        latitude = latitude_number
    else:
        raise ValueError("Latitude number must be in the range 0 to 180.")

    # Check if longitude number is within range [0, 360]
    if 0 <= longitude_number <= 360:
        longitude = longitude_number
    else:
        raise ValueError("Longitude number must be in the range 0 to 360.")

    # Determine if it's in the Northern or Southern Hemisphere
    if latitude_number < 90:
        latitude = 90 - latitude_number
    else: 
        latitude = latitude_number - 180

    # Determine if it's in the Eastern or Western Hemisphere
    if longitude_number < 180:
        longitude = longitude_number
    else:
        longitude = longitude_number - 360

    return latitude, longitude

# Example usage:
#latitude_number = ilat  # Example latitude number between 0 and 180
#longitude_number = ilon  # Example longitude number between 0 and 360

#latitude, longitude = convert_to_lat_lon(latitude_number, longitude_number)
#latitude, longitude = convert_ilatlon_to_latlon(ilat, ilon)

#print(f"Latitude: {latitude} N, Longitude: {longitude} W")