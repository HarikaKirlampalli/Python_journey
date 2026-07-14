import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime

#Initialize Voice Engine
engine = pyttsx3.init()

def speak(Text):
    engine.say(Text)
    engine.runAndWait()

def take_commands():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except Exception as e:
        print("Sorry, please say that again.")
        print(e)          
        return ""
    
def wish_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning \nI am Your Virtual Assistant")
    elif hour < 18:
        speak("Good Afternoon \nI am Your Virtual Assistant")
    else:
        speak("Good Evening \nI am Your Virtual Assistant")
wish_user()

while True:
    command = take_commands()
    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(command,2)
        print(info)
        speak(info)
    elif "exit" in command:
        speak("Goodbye")
        break













            
