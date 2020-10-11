
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
from email.header import decode_header
import webbrowser
import os
import readmail
import whatsapp
import API_list as API
import music_player as music
import emailAPI
import sms


def SpeakText(command): 
	
	# Initialize the engine 
	engine = pyttsx3.init() 
	engine.say(command) 
	engine.runAndWait() 
	
SpeakText("Welcome to the voice, your personal assistant")
'''detector = ObjectDetection()

model_path = "./model/yolo-tiny.h5"
input_path = "./input/NewPicture.jpg"
output_path = "./output/newimage.jpg"

detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath(model_path)
detector.loadModel()
import cv2

videoCaptureObject = cv2.VideoCapture(0)'''







main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "Chennai"
API_KEY = "87950af400adc37ba457d4bd7bc07a27"
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

emaildb={
        "jackson":"siddharth.dash07@gmail.com",
        "jonathan":"siddharth.d.wisekreator@gmail.com"
        
        }

whatsappdb={
        "siddharth":"+919176136743"
        
        }


r = sr.Recognizer() 



	


while(1):
    
    '''menu for tasks'''
    try:
        with sr.Microphone() as source2:
            print("noise redn")
            r.adjust_for_ambient_noise(source2, duration=0.5)
            print("listening")
            audio2 = r.listen(source2)
            print("converting")
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print("Did you say "+MyText)
            
            a = MyText.split(" ")
            print(a)
        if "read" in a and "email" in a:
            readmail.readmymail()    

        elif "email" in a:
            emailAPI.send_email()


        elif "weather" in a:
            API.weather_api()
               
        elif "news" in a:
            API.news_api()
        elif "time" in a:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            SpeakText(current_time)
        elif "date" in a:
            today = date.today() 
            print("Today date is: ", today)
            SpeakText(today)
        elif "calculator" in a:
            calc.calculator()
        
        elif "song" in a or "music" in a:
            music.play_music()
        
        elif "detect" in a:
            result = True
            while(result):
                ret,frame = videoCaptureObject.read()
                cv2.imwrite("./input/NewPicture.jpg",frame)
                result = False
            videoCaptureObject.release()
            cv2.destroyAllWindows()
            detection = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path)
            for eachItem in detection:
                print(eachItem["name"] , " : ", eachItem["percentage_probability"])
        elif "whatsapp" in a:
            SpeakText("Who is the receiver")
            try:
                with sr.Microphone() as source2:
                    audio2 = r.listen(source2)
                    receive = r.recognize_google(audio2)
                    print(receive)
            except sr.UnknownValueError:
                SpeakText("message was not clear")
            
            if receive.lower() in whatsappdb:
                receive=receive.lower()
                phno=whatsappdb[receive]
                SpeakText("say your message")
                try:
                    with sr.Microphone() as source2:
                        audio2 = r.listen(source2)
                        message = r.recognize_google(audio2)
                        print(message)
                except sr.UnknownValueError:
                    SpeakText("message was not clear")
                
                whatsapp.whatsappmsg(message,phno)
            else:
                SpeakText("receiver not available")
        elif "message" in a or "sms" in a:
            SpeakText("Who is the receiver")
            try:
                with sr.Microphone() as source2:
                    audio2 = r.listen(source2)
                    receive = r.recognize_google(audio2)
                    print(receive)
            except sr.UnknownValueError:
                SpeakText("message was not clear")
            
            if receive.lower() in whatsappdb:
                receive=receive.lower()
                phno=whatsappdb[receive]
                SpeakText("say your message")
                try:
                    with sr.Microphone() as source2:
                        audio2 = r.listen(source2)
                        message = r.recognize_google(audio2)
                        print(message)
                except sr.UnknownValueError:
                    SpeakText("message was not clear")
                
                sms.send_sms(message,phno)
            else:
                SpeakText("receiver not available")
        
        
            
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occured")
    