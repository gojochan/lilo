from logging import exception
from time import strftime

import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

engine = pyttsx3.init()

def say(text):
    engine.say(text)
    engine.runAndWait()
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=0.8 #default
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query=r.recognize_google(audio,language='en-in')
            print(f"user said: {query}")
            return query
        except exception as e:
            return "some error occurred . sorry from lilo"

if __name__ == "__main__":
    print("PyCharm")
    say("Hello, I love mommy")
    print("listening...")
    query=takecommand()
    sites=[["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"]]#making lilo to do different task
    for site in sites:
        if f"open {site[0]}".lower() in query.lower():
            say(f"openning {site[0]} sir..")
            webbrowser.open(site[1])
    if "the time" in query:
        strftime= datetime.datetime.now().strftime("%H:%M:%S")
        say(f"the time is {strftime}")

    #say(query)


