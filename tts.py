
import calc
import operator
import smtplib 
import requests, json 
from datetime import datetime
from datetime import date
import speech_recognition as sr 
import pyttsx3
from pygame import mixer  


main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "Chennai"
API_KEY = "87950af400adc37ba457d4bd7bc07a27"
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY


r = sr.Recognizer() 


def SpeakText(command): 
	
	# Initialize the engine 
	engine = pyttsx3.init() 
	engine.say(command) 
	engine.runAndWait() 
	
	


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
            
#sending email
        if "email" in a:
            s = smtplib.SMTP('smtp.gmail.com', 587) 
            s.starttls() 
            s.login("siddhu.dash@gmail.com", "65477412") 
            SpeakText("Please say your message")
            try:
                with sr.Microphone() as source2:
                    audio2 = r.listen(source2)
                    message = r.recognize_google(audio2)
            except sr.UnknownValueError:
                SpeakText("message was not clear")
            SpeakText("Sending")
            s.sendmail("siddhu.dash@gmail.com", "siddharth.dash07@gmail.com", message) 
            s.quit() 
            
            print("email sent")

#weather info
        if "weather" in a:
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
               # showing the error message
               print("Error in the HTTP request")
               
        if "news" in a:
            
            open_bbc_page = requests.get(main_url).json()
            article = open_bbc_page["articles"]
            results = []
            for ar in article:
                results.append(ar["title"])
            
            for i in range(len(results)-5):
                print(i+1,results[i])
                SpeakText(results[i])
        if "time" in a:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            SpeakText(current_time)
        if "date" in a:
            today = date.today() 
            print("Today date is: ", today)
            SpeakText(today)
        if "calculator" in a:
            calc.calculator()
        if "song" in a:
            mixer.init() 
            mixer.music.load("song.mp3") 
            mixer.music.set_volume(0.7) 
            mixer.music.play() 
            while True: 
                  
                print("Press 'p' to pause, 'r' to resume") 
                print("Press 'e' to exit the program") 
                query = input("  ") 
                  
                if query == 'p': 
                    mixer.music.pause()      
                elif query == 'r': 
                    mixer.music.unpause() 
                elif query == 'e': 
                    mixer.music.stop() 
                    break
            
        
            
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occured")
    