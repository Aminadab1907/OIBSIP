"""
Project Name: Weather App with GUI
Project Objective: To create weather app with a simple GUI using the "tkinterbootstrap'
 library that fetches for the GUI design and display scurrent weather data for a
 user-specified location using the OpenWeatherMap API
Project Key Features: Fetching current weather data (temperature, humidity, weather description) for a specified city.

** We will make use of teh OpenWeatherMap API free plan to have
access to real-time weather data through HTTP Calls

"""


import tkinter as tk
from ttkbootstrap import Style
from tkinter import ttk
import requests


# Create our main function to get the weather data
# of a city upon receiving the city name as an argument
# for the next function
# using an HTTP call to the openweathermap API

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

def fetch_weather():
    # The input for the city name is provided here, and then capitalized
    city = city_entry.get().capitalize()

    # It calls the get_city_weather() function, passing the city name as an argument. This function is responsible
    # for fetching weather data for the specified city.
    weather = get_city_weather(city)

    # If the get_city_weather() function returns a non-empty result (i.e., weather data is available for the
    # specified city), it prints out the weather information, including temperature, humidity, and weather
    # description, using formatted strings.
    if weather:
        result_label.config(text=f"     {city}:\n"
                                  f"Temperature: {weather['Temperature']}°C\n"
                                  f"Humidity: {weather['Humidity']}%\n"
                                  f"Weather: {weather['Weather']}")

    # If the get_city_weather() function returns None (indicating that the city was not found or there was an error
    # fetching weather data), it prints a message indicating that the city was not found or there was an error.
    else:
        result_label.config(text="City not found or error fetching weather data.")

# Create the main application window
root = tk.Tk()
root.title("Weather App")

# Load the bootstrap style
style = Style(theme='cyborg')

# Create a frame to hold the input fields and button
frame = ttk.Frame(root, padding="20", style="solar.TFrame")
frame.grid(row=0, column=0, padx=10, pady=10)

# City entry field
city_label = ttk.Label(frame, text="City", style="info.TLabel")
city_label.grid(row=0, column=0, sticky="w")

city_entry = ttk.Entry(frame, width=30, style="info.TEntry")
city_entry.grid(row=0, column=1, padx=5)

# Button to fetch weather data
fetch_button = ttk.Button(frame, text="Fetch Weather", command=fetch_weather, style="success.TButton")
fetch_button.grid(row=1, column=0, columnspan=2, pady=10)

# Label to display weather result
result_label = ttk.Label(root, wraplength=400, style="lumen.TLabel")
result_label.grid(row=1, column=0, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
