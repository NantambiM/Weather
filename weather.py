import requests
from dotenv import load_dotenv
import os
from pprint import pprint#this helps to format the json we receive from the api into a readable format

load_dotenv()

def get_current_weather(city="Kampala"):
    
    requesturl=f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=metric"

    weather_data=requests.get(requesturl).json()
   
    return weather_data
    

if __name__=="__main__":
    print("\n*** Get Current Weather Conditions ***\n")

    city=input("Please enter a city name:\n")

    #check for empty string or string with only spaces
    if not bool(city.strip()):
        city="Kampala"

    weather_data=get_current_weather(city)
    print(f"Current weather for {weather_data['name']}")
    print(f"Current temperature for {weather_data['main']['temp']}°C")
    print(f"Feels like {weather_data['main']['feels_like']} and {weather_data['weather'][0]['description']}.")
