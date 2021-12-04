# -*- coding: utf8 -*
import requests
import json
import urllib
import webbrowser
import time
import random
import os
import sqlite3
from datetime import datetime as dt
import time
from art import *
from couleur import *


def Weather():
    system("clear")
    print(Color.blue_bold)
    tprint("Meteo")
    print(Color.white_bold+"\n")

    key = '198fc752bfe61462867c976ed4658a0a'
    
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    GPS = ("coordone",)
    cur.execute("SELECT * FROM settings WHERE settingName = ?",GPS)
    for item in cur:
        coo = item[1]
        coo = coo.split(' ')
        lat = coo[0]
        lon = coo[1]

    if key is None:
        # URL de test :
        METEO_API_URL = "https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx"
    else: 
        # URL avec clé :
        METEO_API_URL = "https://api.openweathermap.org/data/2.5/forecast?lat="+lat+"&lon="+lon+"&appid=" + key

    response = requests.get(METEO_API_URL)
    content = json.loads(response.content.decode('utf-8'))

    data = [] # On initialise une liste vide
    for prev in content["list"]:
        datetime = prev['dt'] * 1000
        weather = prev['weather'][0]['main']

        temperature = int(prev['main']['temp'] - 273.15) # Conversion de Kelvin en °c
        temperature = round(temperature, 2)
        data.append([datetime, temperature])

    if prev['weather'][0]['main'] == 'Rain':
        if prev['weather'][0]['description'] == 'light rain':
            weather = 'une légère pluie.'
        else:
            weather = 'de la pluie'
    if prev['weather'][0]['main'] == 'Clouds':
        if 'scattered' in prev['weather'][0]['description']:
            weather = 'des nuages dispersés.'
        elif 'overcast' in prev['weather'][0]['description']:
            weather = 'un ciel nuageux.'
        elif 'broken' in prev['weather'][0]['description']:
            weather = 'des nuages brisés.'
        elif 'few' in prev['weather'][0]['description']:
            weather = 'quelque nuages.'
        else:
            weather = 'des nuages.'
    if prev['weather'][0]['main'] == 'Clear':
        weather = 'un ciel dégagé.'

    if prev['weather'][0]['main'] == 'Snow':
        weather = 'un petit peut de neige.'

    if prev['weather'][0]['description'] == 'Mist':
        if 'light' in prev['weather'][0]['description']:
            weather = 'un ciel dégagé.'

    meteo = '        Il fait '+str(temperature)+'°C avec '+str(weather)

    print(Color.yellow_bold+meteo)
    fin = input("")