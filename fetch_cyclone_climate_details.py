import requests  # Import the requests library to handle HTTP requests
import json  # Import the json library to handle JSON data

def fetch_windy_data(api_key, lat, lon, model, parameters, levels=None):
    # Define the Windy API endpoint URL
    url = "https://api.windy.com/api/point-forecast/v2"
    
    # Define the headers for the HTTP request, specifying the content type as JSON
    headers = {
        'Content-Type': 'application/json'
    }
    
    # Construct the body of the request with the required parameters
    body = {
        "lat": lat,  # Latitude of the location
        "lon": lon,  # Longitude of the location
        "model": model,  # Weather model to use (e.g., "gfs")
        "parameters": parameters,  # List of weather parameters to fetch
        "levels": levels,  # List of pressure levels (optional)
        "key": api_key  # Your API key
    }
    
    # Send a POST request to the Windy API endpoint with the headers and body
    response = requests.post(url, headers=headers, data=json.dumps(body))
    
    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # If the request is successful, parse the JSON response
        data = response.json()
        return data  # Return the parsed data
    else:
        # If the request fails, raise an exception with the error message
        raise Exception(f"Error {response.status_code}: {response.text}")

# Example usage
api_key = "your_API_key"  # Your Windy API key
lat = 49.809  # Latitude of the desired location
lon = 16.787  # Longitude of the desired location
model = "gfs"  # Weather model to use (e.g., "gfs")
parameters = ["wind", "dewpoint", "rh", "pressure"]  # List of parameters to fetch
levels = ["surface", "800h", "300h"]  # List of pressure levels to fetch

try:
    # Call the fetch_windy_data function with the provided parameters
    data = fetch_windy_data(api_key, lat, lon, model, parameters, levels)
    # Print the fetched data in a pretty JSON format
    print(json.dumps(data, indent=4))
except Exception as e:
    # Print any errors that occur during the request
    print(e)
