
import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
import time

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)
rate = engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def alarm(query):
    timehere = open("Alarmtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

def next_video():
    pyautogui.hotkey('shift', 'n')
    speak("Playing Next video")

def type_youtube_search(query):
    pyautogui.click(x=500, y=200)  # Adjust these coordinates based on your screen
    pyautogui.write(query)
    pyautogui.press("enter")
    speak(f"Searching for {query} on YouTube")

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir, You can call me anytime")
                    break

                # ... other commands ...

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("Video paused")

                elif "play" in query:
                    pyautogui.press("k")
                    speak("Video played")

                elif "mute" in query:
                    pyautogui.press("m")
                    speak("Video muted")

                elif "next video" in query:
                    next_video()

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up, sir")
                    volumeup()

                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)

                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)

                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)

                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                elif "temperature" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current {search} is {temp}")

                elif "weather" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current {search} is {temp}")

                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done, sir")

                elif "Write on Search " in query:
                    speak("What do you want to search for on YouTube?")
                    search_query = takeCommand().lower()
                    type_youtube_search(search_query)

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")

                elif "finally sleep" in query:
                    speak("Going to sleep, sir")
                    exit()
