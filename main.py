import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def say(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    print("PyCharm")
    say("Hello, I am Lilo AI")


