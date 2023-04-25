from tkinter import *
from configparser import ConfigParser
import requests


url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']


def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        # (city, country, temp_celsius, temp_fahrenheit, icon, weather)
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        temp_fahrenheit = (temp_kelvin - 273.15) * 9/5 + 32
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        final = (city, country, temp_celsius, temp_fahrenheit, icon, weather)
        return final
    else:
        return None


def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        locaction_label.config(text=f"{weather[0]}, {weather[1]}")
        temperature_label.config(text=f"Temperature: {weather[2]:.1f}°C / {weather[3]:.1f}°F")
        weather_label.config(text=f"Weather: {weather[5]}")
        icon_url = f"http://openweathermap.org/img/w/{weather[4]}.png"
        icon_data = requests.get(icon_url).content
        with open("icon.png", "wb") as f:
            f.write(icon_data)
        image.config[bitmap]='icons/{}.png'.format(weather[4])
    else:
        locaction_label.config(text="Invalid city name")
        temperature_label.config(text="")
        weather_label.config(text="")
        image.config(bitmap="")


app = Tk()
app.title("WEATHER-app")
app.geometry('700x300')

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn = Button(app, text='Search weather', width=12, command=search)
search_btn.pack()

locaction_label = Label(app, text='', font=('bold', 20))
locaction_label.pack()

image = Label(app, bitmap='')
image.pack()

temperature_label = Label(app, text='')
temperature_label.pack()

weather_label = Label(app, text='')
weather_label.pack()

app.mainloop()
