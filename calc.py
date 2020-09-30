# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 16:22:00 2020

@author: SIDDHARTH RAJ DASH
"""


def calculator():
    import operator
    import speech_recognition as s_r
    import pyttsx3
    def SpeakText(command): 
	
    	# Initialize the engine 
    	engine = pyttsx3.init() 
    	engine.say(command) 
    	engine.runAndWait() 
    r = s_r.Recognizer()
    my_mic_device = s_r.Microphone(device_index=1)
    with my_mic_device as source:
        SpeakText("Say what you want to calculate, example: 3 plus 3")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    my_string=r.recognize_google(audio)
    SpeakText(my_string+" is")
    def get_operator_fn(op):
        return {
            '+' : operator.add,
            '-' : operator.sub,
            'x' : operator.mul,
            'divided' :operator.__truediv__,
            'Mod' : operator.mod,
            'mod' : operator.mod,
            '^' : operator.xor,
            'into':operator.mul
            }[op]
    def eval_binary_expr(op1, oper, op2):
        op1,op2 = int(op1), int(op2)
        return get_operator_fn(oper)(op1, op2)
    SpeakText(eval_binary_expr(*(my_string.split())))