from cgi import print_arguments
from email.mime import audio
from time import strftime
from unittest import result
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import sys

print("initializing Asisten terbaikmu")

MASTER = "Muhammad Syifa"

engine = pyttsx3.init("sapi5")
rate = engine.getProperty('rate')
engine.setProperty('rate', 140)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


#speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

#function
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("Good Morning" + MASTER)
    
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + MASTER)
    
    else: 
        speak("Good Evening"+ MASTER)
        speak("")


#microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source) 

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language="en-us")
        print(f"user said: {query}\n")
    except Exception as e:
        print("say that again please")
        query = None

    return query

query = takeCommand()
speak("Hello my name is Jeki")
wishMe()
speak("what do you want"+ MASTER)

def run_jarvis():
    #main start here
    
    query = takeCommand()

    #logic for task as per query
    if "wikipedia" in query.lower():
        speak("searching wikipedia...")
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        print(result)
        speak(result)
    
    elif "open youtube" in query.lower():
        url = "youtube.com"
        edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
        webbrowser.get(edge_path).open(url)

    elif 'play' in query.lower():
        song = query.replace("play", "")
        speak("yes"+MASTER)
        speak("playing"+ song +", enjoy the music")
        print("playing "+ song)
        pywhatkit.playonyt(song)
        
        sys.exit()
    
    elif "song" in query.lower():
        songs_dir = "C:\\Users\\asus\\Downloads\\Music"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif "the time" in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")

    elif "open instagram" in query.lower():
        url = "instagram.com"
        edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
        webbrowser.get(edge_path).open(url)

    elif "thank you" in query.lower():
        speak("Your welcome {MASTER} i want sleeping now")
        sys.exit()

    elif "to sleep" in query.lower():
        speak("yes "+MASTER+", Have a good night's sleep")
        speak("thank you for today and enjoy the music"+MASTER)
        url = "https://youtu.be/cQGfLDnmWS8"
        edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
        webbrowser.get(edge_path).open(url)
        sys.exit()

    else:
        speak("not any intruction")
        print(query)

while True:   
    MASTER = "Sir"
    mendengarkan = sr.Recognizer()
    engine = pyttsx3.init("sapi5")
    #kecepatan baca
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 140)
    #jenis suara [0] male [1] female
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    run_jarvis()