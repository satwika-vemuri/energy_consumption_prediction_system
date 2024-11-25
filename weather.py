import requests

# WeatherAPI key
WEATHER_API_KEY = '8765384b659e4514b6f221411241611'  # TODO: Replace with your own WeatherAPI key

def get_weather(city):
    # TODO: Build the API request URL using the base API endpoint, the API key, and the city name provided by the user.
    params = {
	'key' : WEATHER_API_KEY,
	'q' : city
    }
    # TODO: Make the HTTP request to fetch weather data using the 'requests' library.
    response = requests.get("http://api.weatherapi.com/v1/current.json",params)
    # TODO: Handle HTTP status codes:
    # - Check if the status code is 200 (OK), meaning the request was successful.
    # - If not 200, handle common errors like 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), and any other relevant codes.
    
    if response.status_code == 200:
        # TODO: Parse the JSON data returned by the API. Extract and process the following information:
        data = response.json()
        # - Current temperature in Fahrenheit
        outdoor_temp = data['current']['temp_f']
	# - The "feels like" temperature
        feels_like = data['current']['feelslike_f']
	
        # TODO: Display the extracted weather information in a well-formatted manner.
        print(f"Weather data for {city} ...")
        print(f"Status 200: {response.status_code}")
        print(f"Outdoor Temperature: {outdoor_temp} F (Feels Like: {feels_like} F)")
        
    else:
        # TODO: Implement error handling for common status codes. Provide meaningful error messages based on the status code.
        if (response.status_code==404):
                print(f"Error: {response.status_code}. Not Found.")
        elif (response.status_code==401):
                print(f"Error: {response.status_code}. Unauthorized.") 
        elif (response.status_code==400):
                print(f"Error: {response.status_code}. Bad Request.")
        else:
                print(f"Error: {response.status_code}. Something went wrong.")

if __name__ == '__main__':
    # TODO: Prompt the user to input a city name.
    city_name = input("Enter city name: ")
    # TODO: Call the 'get_weather' function with the city name provided by the user.
    get_weather(city_name)
    pass
 
