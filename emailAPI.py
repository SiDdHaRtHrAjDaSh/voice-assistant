# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 04:22:58 2020

@author: SIDDHARTH RAJ DASH
"""
import speech_recognition as sr 
import pyttsx3
import smtplib 

r = sr.Recognizer() 
emaildb={
        "jackson":"siddharth.dash07@gmail.com",
        "jonathan":"siddharth.d.wisekreator@gmail.com"
        
        }
def SpeakText(command): 
	
	# Initialize the engine 
	engine = pyttsx3.init() 
	engine.say(command) 
	engine.runAndWait() 
def send_email():
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("siddhu.dash@gmail.com", "65477412") 
    SpeakText("Please say the receiver's name")
    
    try:
        with sr.Microphone() as source2:
            audio2 = r.listen(source2)
            receive = r.recognize_google(audio2)
            print(receive)
    except sr.UnknownValueError:
        SpeakText("message was not clear")
    if receive.lower() in emaildb:
        receive=receive.lower()
        emailid=emaildb[receive]
        SpeakText("Please say your message")           
        try:
            with sr.Microphone() as source2:
                audio2 = r.listen(source2)
                message = r.recognize_google(audio2)
        except sr.UnknownValueError:
            SpeakText("message was not clear")
        SpeakText("Sending")
        s.sendmail("siddhu.dash@gmail.com", emailid, message) 
        s.quit() 
        
        print("email sent")