from logging import exception

import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def say(text):
    engine.say(text)
    engine.runAndWait()
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        audio = r.listen(source)
        try:
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
    say(query)


