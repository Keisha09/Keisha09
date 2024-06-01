import tkinter as tk
from tkinter import messagebox
import requests
api_key="f4c9fbe90830d521c6bda58201a67722"
base_url="http://api.openweathermap.org/data/2.5/weather?"
city="London"
complete_url=base_url+"appid="+api_key+"&q="+city+"&units=metric"
response=requests.get(complete_url,timeout=10)
data=response.json()
def get_weather(city):
    if data["cod"]!=404:
        main=data["main"]
        weather=data["weather"][0]
        temp=main["temp"]
        pressure=main["pressure"]
        humidity=main["humidity"]
        description=weather["description"]
        weather_info=f"Temperature: {temp} C\n Pressure: {pressure}\n Humidity: {humidity}\n Description:{description}"
    else:
        weather_info="City Not Found"
    return weather_info
def show_weather():
    city = city_entry.get()
    weather_info = get_weather(city)
    weather_label.config(text=weather_info)
root = tk.Tk()
root.title("Weather App")
tk.Label(root, text="Enter city name:").pack(pady=10)
city_entry = tk.Entry(root)
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=show_weather).pack(pady=10)
weather_label = tk.Label(root, text="", font=("Helvetica", 14))
weather_label.pack(pady=20)
tk.Button(root, text="Exit", command=root.quit).pack(pady=10)
root.mainloop()