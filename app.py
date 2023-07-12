from flask import Flask,redirect, url_for,request, render_template,flash,jsonify,session
import pyttsx3
import speech_recognition as sr
import os
app = Flask(__name__)

r = sr.Recognizer()

def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

@app.route('/')
def hello():
    while(1):   
        try:
             
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                 
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)
                 
                #listens for the user's input
                audio2 = r.listen(source2)
                 
                # Using google to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
         
                print("Did you say ",MyText)
                SpeakText(MyText)
                 
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
             
        except sr.UnknownValueError:
            print("unknown error occurred")  
    return render_template('index.html',text=MyText)