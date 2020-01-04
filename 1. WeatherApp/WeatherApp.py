#WeatherApp based from Keith Galli: https://github.com/KeithGalli/GUI/

import tkinter as tk
import requests
from tkinter import font
import sys

# Window height and width
HEIGHT = 400
WIDTH = 500


# Querey the city data from Open Weather Map
def get_weather(city):
    weather_key = '58879621806c68110e4d04b4fc347452'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params = params)
    weather = response.json()
    print(weather)
    label['text'] = format_response(weather) 

# Format response to visual data
def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        min_temp = weather['main']['temp_min']
        max_temp = weather['main']['temp_max']
        final_string = 'City: %s \nConditions: %s \nCurrent Temperature: %s \nLow: %s \nHigh: %s' % (name, desc, temp, min_temp, max_temp)
    except:
        final_string = "There was an error! \nPlease try again :)"
        
    return final_string

# Set Canvas
root = tk.Tk()
root.title('Weather App')
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# Set Background
background_image = tk.PhotoImage(file = 'Images/earth.png')
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth = 1, relheight = 1)

# Set Upper Frame
upper_frame = tk.Frame(root, bg = '#ff9999', bd = 5)
upper_frame.place(relx = .5, rely = .1, relwidth = .75, relheight = .1, anchor = 'n')

# Set Text Box
entry = tk.Entry(upper_frame, font = 40)
entry.place(relwidth = .65, relheight = 1)

# Set Button
button = tk.Button(upper_frame, text = "Get Weather", font = 40, command = lambda: get_weather(entry .get()))
button.place(relx = 0.7, relheight = 1, relwidth = .3)

# Set Response Frame
lower_frame = tk.Frame(root, bg = '#ff9999', bd = 10)
lower_frame.place(relx = .5, rely = .25, relwidth = .75, relheight = .6, anchor = 'n')

# Set Response Label
label = tk.Label(lower_frame, text = "", bg = 'white', font = ('Casteller', 20))
label.place(relwidth = 1, relheight = 1)


# Exit Button
exit_button = tk.Button(root, text = "Exit", font = 20, command = root.destroy).place(relx = .5, rely = .9)

root.mainloop()
 





