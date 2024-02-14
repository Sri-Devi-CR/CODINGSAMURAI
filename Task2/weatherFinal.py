"""
CODING SAMURAI - PYTHON DEVELOPMENT INTERNSHIP (TASK 2)

Project Title: Weather Forecast Application
Project Description: Create a simple command-line weather forecast application
in Python that provides users with current weather information for a specified location.
This project will involve making API requests, parsing JSON data, and displaying the information to the user.

Key Features you can include:
    Location input: Allow users to enter a city or location for which they want to get the weather forecast.
    API Integration: Use a weather API (e.g., OpenWeatherMap) to fetch current weather data for the specified location.
    Display weather data: Present the weather information to the user,
            including temperature, humidity, wind speed, and weather conditions (e.g., sunny, cloudy, rainy).
    Unit conversion: Provide options for users to choose between Celsius and Fahrenheit for temperature units.
    Error handling: Handle cases where the user enters an invalid location or the API request fails gracefully.
"""

import tkinter as tk
from tkinter import *
import requests
from tkinter import messagebox
from PIL import Image, ImageTk

FONT1 = ("Lexend", 20)
FONT2 = ("Lexend", 18)
FONT_BUTTON = ("Lexend", 10)
FONT3 = ("Lexend", 25)

BG1 = '#9CC0E7'

def get_weather(city):
    API_KEY = "531b6fb96e73337c567718749ee6633a"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error","City Not Found")
        return None

    try:
        weather_json = res.json()
        city = weather_json['name']
        country = weather_json['sys']['country']

        icon_id = weather_json['weather'][0]['icon']
        icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
        
        temperature = weather_json['main']['temp'] - 273.15
        humidity = weather_json['main']['humidity']
        wind_speed = weather_json['wind']['speed']
        description = weather_json['weather'][0]['description']
        
        return (city, country, icon_url, temperature, humidity, wind_speed, description)

    except:
        messagebox.showerror("Error", "Cannot retrieve weather data")
        return


def search_city():
    city = city_ip.get()
    result = get_weather(city)
    if result is None:
        return
    
    city, country, icon_url, temp, humidity, wind_speed, desc = result
    
    location_lab.configure(text=f"{city}, {country}")
    
    img_open = Image.open(requests.get(icon_url, stream=True).raw)
    img = ImageTk.PhotoImage(img_open)
    icon_lab.config(image=img)
    icon_lab.image = img

    temp_lab.configure(text=f"Temperature : {temp:.2f}°C")
    humi_lab.configure(text=f"Humidity: {humidity}")
    wind_sp_lab.configure(text=f"Wind Speed: {wind_speed}")
    desc_lab.configure(text=f"Description : {desc}")

root = tk.Tk()
root.config(background=BG1)
root.title("Weather app")
root.geometry("600x500+150+100")

city_lab = Label(root,text="Enter the city", font=FONT1, background=BG1)
city_lab.pack(pady=20)

city_ip = Entry(root,font=FONT2)
city_ip.pack(pady=10)

search = Button(root, text="Search", font=FONT_BUTTON, command=search_city, background="#DAC778")
search.pack()

#pplaceholders for the info to display
location_lab = Label(root,font=FONT3, background=BG1)
location_lab.pack(pady=20)

#weat[weather][0][icon]
icon_lab = Label(root, background=BG1)
icon_lab.pack()

#wea['main]['temp]
temp_lab = Label(root, font=FONT2, background=BG1)
temp_lab.pack()

#wea['main]['humidity]
humi_lab = Label(root, font=FONT2, background=BG1)
humi_lab.pack()

#wea[wind][speed]
wind_sp_lab = Label(root,font=FONT2, background=BG1)
wind_sp_lab.pack()

#wea[weather][0][description]
desc_lab = Label(root, font=FONT2, background=BG1)
desc_lab.pack()

root.mainloop()