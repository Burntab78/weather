# Author: Bryan Burnett
# Date: Can't get a date, created on 4-18-24
# Description: Weather app using the OpenWeatherMap API.

# import our imports
import requests

# api key generated from openweathermap.org
api_key ='37d17042e2d2ed367b57efe898e6a359'

# get user input
user_input = input("Which city: ")

# Test to ensure api working --commented out after test.
# print (user_input)

# weather data from openweathermap.org using fstring to get website information
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

# lastly, put in some error handling. -- 'cod' being resource in the api, and '404' being not found.
if weather_data.json()['cod'] == '404':
    print("No city found.")
else:

# test the status code --commented out after test.
# print (weather_data.status_code)

# Run the app using weather_data.json -- will generate a lot of info --commented out after run to clean up.
# print(weather_data.json())

# make the generated info, more pertinent/ pretty.
# get the weather conditions (can be altered depending on what info wanted.)
    weather = weather_data.json()['weather'][0]['main']
# get the temperature -- commented out after run to clean up.
# temp = weather_data.json()['main']['temp']
# cleaned up line -- round to round up the temperature and get rid of the float number.
    temp = round(weather_data.json()['main']['temp'])

# print results --commented out after run to clean up.
# print(weather, temp), in a normal sentence.
    print(f"The weather conditions in {user_input} is: {weather}")
    print(f"The tempurature in {user_input} is: {temp}ºF")
