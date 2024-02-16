"""
Project Name: Weather App
Project Objective: To create a command-line weather app that fetches and displays
current weather data for a user-specified location using the OpenWeatherMap API
Project Key Features: Fetching current weather data (temperature, humidity, weather description) for a specified city.

** We will make use of teh OpenWeatherMap API free plan to have
access to real-time weather data through HTTP Calls

"""

# Import the necessary library
import requests  # An HTTP library to make a request from a website (in our case OpenWeatherMap API Website)


# Create our main function to get the weather data
# of a city upon receiving the city name as an argument
# for the next function

def get_city_weather(city):
    # API key provided by OpenWeatherMap
    api_key = 'e1e4383c2e0f14700eab2888b652f01b'
    # Endpoint URL for our API requests
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    # Send an HTTP GET request to the URL specified above by the 'url' variable
    # A response object will be generated representing a response from the server
    response = requests.get(url)

    # JSON data is extracted from the response received from the server
    # and is returned as a python dictionary
    # and the variable json_data will contain the weather data for the specified
    # city in the form of a python dictionary
    json_data = response.json()

    # A debugging code to check that json data is received correctly
    # for the desired city
    # Uncomment for debugging

    # -------------------------------------
    print("Retrieved JSON data:")
    print(json_data)
    # -------------------------------------

    # This conditional snippet checks the status code (cod) returned by the API.A status code of 200 indicates that
    # the request was successful and that the response contains valid data.
    if json_data['cod'] == 200:

        # If the status code is 200, the code extracts relevant weather information from the JSON response and stores
        # it in a dictionary called weather_data. The temperature (main.temp), humidity (main.humidity), and weather
        # description (weather[0].description) are extracted from the JSON data.
        weather_data = {
            'Temperature': json_data['main']['temp'],
            'Humidity': json_data['main']['humidity'],
            'Weather': json_data['weather'][0]['description']
        }
        return weather_data

        # If the status code is not 200 (i.e., there was an error or the city was not found), the function returns
        # None to indicate that no weather data is available for the specified city.
    else:
        return None


def main():
    # It prompts the user to input the name of the city for which they want to retrieve weather information.
    city = input("Enter city name:  ").capitalize()

    # It calls the get_city_weather() function, passing the city name as an argument. This function is responsible
    # for fetching weather data for the specified city.
    weather = get_city_weather(city)

    # If the get_city_weather() function returns a non-empty result (i.e., weather data is available for the
    # specified city), it prints out the weather information, including temperature, humidity, and weather
    # description, using formatted strings.
    if weather:
        print(f"Weather in {city}:")
        print(f"\tTemperature: {weather['Temperature']}°C")
        print(f"\tHumidity: {weather['Humidity']}%")
        print(f"\tWeather: {weather['Weather']}")

    # If the get_city_weather() function returns None (indicating that the city was not found or there was an error
    # fetching weather data), it prints a message indicating that the city was not found or there was an error.
    else:
        print("City not found or error fetching weather data.")


if __name__ == "__main__":
    main()
