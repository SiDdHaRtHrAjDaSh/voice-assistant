# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 04:01:04 2020

@author: SIDDHARTH RAJ DASH
"""

import calc
import operator
import smtplib 
import requests, json 
from datetime import datetime
from datetime import date
import speech_recognition as sr 
import pyttsx3
from pygame import mixer  
from imageai.Detection import ObjectDetection
import imaplib
import email

main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "Chennai"
API_KEY = "87950af400adc37ba457d4bd7bc07a27"
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

def SpeakText(command): 
	

	engine = pyttsx3.init() 
	engine.say(command) 
	engine.runAndWait() 

def weather_api():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']-273
        humidity = main['humidity']
        pressure = main['pressure']
        report = data['weather']
        formatted_temp = "{:.2f}".format(temperature)
        SpeakText("Todays forecast for "+CITY)
        SpeakText("The temperature is "+formatted_temp+"degrees")
        SpeakText("The humidity is "+str(humidity))
        SpeakText("The pressure is "+str(pressure))
        SpeakText("The forecast is "+str(report[0]['description']))
    else:
        print("Error in the HTTP request")

def news_api():
    open_bbc_page = requests.get(main_url).json()
    article = open_bbc_page["articles"]
    results = []
    for ar in article:
        results.append(ar["title"])
            
    for i in range(len(results)-5):
        print(i+1,results[i])
        SpeakText(results[i])
