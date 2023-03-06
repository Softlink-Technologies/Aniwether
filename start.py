import requests

# API endpoint and API key
url = "http://api.openweathermap.org/data/2.5/weather"
api_key = "<YOUR_API_KEY>"

# User input for city name
city = input("Enter city name: ")

# Parameters for API request
params = {
    "q": city,
    "appid": api_key,
    "units": "metric"
}

# API request
response = requests.get(url, params=params)

# Parsing the JSON response
data = response.json()

# Checking if the response contains weather data
if data["cod"] != "404":
    # Extracting the weather information
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]

    # Displaying the weather information
    print(f"The weather in {city} is {weather}")
    print(f"The temperature is {temperature} degrees Celsius")
    print(f"The temperature feels like {feels_like} degrees Celsius")
else:
    print("City not found.")
