from tkinter import *
import requests
import json


mainWindow = Tk()
mainWindow.title('Weather App')
mainWindow.geometry('300x300')

key = {'YOUR API KEY HERE}

# This will convert Kelvin to Farenheit
def kelvintoF():
    temp_farenheit = 9/5 * (temp - 273) + 32
    return int(temp_farenheit)

# This will get the low temp of the day
def minTemp():
    temp_min = 9/5 * (tempMn - 273) + 32
    return int(temp_min)

# This will get the highest temp of the day
def maxTemp():
    temp_max = 9/5 * (tempMx - 273) + 32
    return int(temp_max)

# This will allow the user to search
# the city of their choice
def search():
# API to pull information asked from the user
    weather_request = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + location.get() + '&appid=' + key)
    forecast = json.loads(weather_request.content)
    find_place = location.get()
    global temp
    global icon
    global tempMn
    global tempMx

# Information that is pulled from the user
    weather = forecast['weather'][0]['main']
    description = forecast['weather'][0]['description']
    icon = forecast['weather'][0]['icon']
    iconP['bitmap'] = 'WeatherIcon/{}.png'.format(icon)
    tempMn = forecast['main']['temp_min']
    tempMx = forecast['main']['temp_max']
    temp = forecast['main']['temp']
    city = forecast['name']
    weatherLabel = Label(mainWindow, text='Weather: ' + weather)
    weatherLabel.grid(row=2, column=0)
    descriptionLabel = Label(mainWindow, text='Today will have ' + description + '\nwith a low of '
                                              + str(minTemp()) + ' and high of ' + str(maxTemp()))
    descriptionLabel.grid(row=3, column=0)
    tempLabel = Label(mainWindow, text='Temp: ' + str(kelvintoF()))
    tempLabel.grid(row=4, column=0)
    cityLabel = Label(mainWindow, text='City: ' + city)
    cityLabel.grid(row=6, column=0)

# Buttons
location = Entry(mainWindow)
location.grid(row=0, column=0, columnspan=2)
location_btn = Button(mainWindow, text='Search', command=search)
location_btn.grid(row=0, column=3)

# This will show the image of the weather
iconP = Label(mainWindow, bitmap='')
iconP.grid(row=1, column=0)

mainWindow.mainloop()

