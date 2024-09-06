#!/usr/bin/env python
# coding: utf-8

# In[3]:


#This application will fetch and display the weather information for a given city.
#Weather Application
#Create a Python application that retrieves and displays current weather information for a given city using a public weather API (e.g., OpenWeatherMap API).

#Steps to Create the Weather Application:
#Set Up Your Environment:

#Install Python on your system if it's not already installed.
#Install necessary libraries such as requests for making HTTP requests and json for handling JSON data.
#Obtain API Key:

#Register on OpenWeatherMap or any other weather service provider.
#Get the API key required to access their weather data.
#Plan the Application Structure:

#Decide on the user interface (CLI or GUI).
#For a Command Line Interface (CLI):
#Input section where the user enters the city name.
#Output section to display weather information.
#For a Graphical User Interface (GUI):
#Use a library like Tkinter to create the input fields and display sections.
#Fetch Weather Data:

#Construct the URL for the API endpoint using the base URL, city name, and API key.
#Make an HTTP GET request to the API endpoint.
#Handle possible exceptions such as network errors or invalid responses.
#Parse the Data:

#Once you receive the JSON response, parse it to extract relevant information like temperature, humidity, weather description, etc.
#Handle various edge cases, such as when the city is not found.
#Display the Data:

#For CLI: Display the fetched weather information in a readable format.
#For GUI: Update the GUI components to show the weather information.
#Implement Error Handling:

#Handle different types of errors such as invalid city names, API limit exceeded, network errors, etc., and display appropriate error messages to the user.
#Optimize the Application:

#Ensure that the API call is made only when necessary (e.g., when the city name changes).
#Cache recent calls to avoid unnecessary API requests.
##Handle large amounts of data efficiently if needed.
#Test Your Application:

#Test the application with multiple city names, including edge cases like misspelled cities or non-existent city names.
#Enhancements (Optional):

#Add features like showing a 5-day weather forecast.
#Display additional information such as wind speed, pressure, etc.
#Implement localization for different languages.

import requests

def get_weather(city, api_key):
    # OpenWeatherMap API URL
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Parameters to be sent to the API
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    
    # Send request to the OpenWeatherMap API
    response = requests.get(base_url, params=params)
    
    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'],
            'wind_speed': data['wind']['speed']
        }
        return weather
    else:
        return None

def display_weather(weather):
    if weather:
        print(f"City: {weather['patna']}")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Description: {weather['description']}")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        print("City not found or error in fetching weather data.")

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"  # Replace with your actual OpenWeatherMap API key
    city = input("Enter the city name: ")
    weather = get_weather(city, api_key)
    display_weather(weather)
import requests
def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['patna'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'],
            'wind_speed': data['wind']['speed']
        }
        return weather
    else:
        return None
def display_weather(weather):
    if weather:
        print(f"City: {weather['city']}")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Description: {weather['description']}")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        print("City not found or error in fetching weather data.")
#Main Program:
#This part of the program asks the user for the city name, calls the get_weather function to fetch the weather data, and then calls the display_weather function to display the data.
        
if __name__ == "__main__":
    api_key = "YOUR_API_KEY"  # Replace with your actual OpenWeatherMap API key
    city = input("Enter the city name: ")
    weather = get_weather(city, api_key)
    display_weather(weather)
#Replace "YOUR_API_KEY" with your actual OpenWeatherMap API key before running the program. When you run the program, it will prompt you to enter the city name and then display the weather information for that city.


# In[ ]:




