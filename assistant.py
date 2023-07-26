# IMPORT LIBRARIES

import pyttsx3  #pip install pyttsx3 
import speech_recognition as sr  #pip install SpeechRecognition
import pytz  #pip install pytz
import wikipedia  #pip install wikipedia
# from googlesearch.googlesearch import GoogleSearch
# import urllib2.request
# import urllib2.response

import datetime
import webbrowser as wb
import os

# FUNCTIONS

engine = pyttsx3.init()

# SPEAK FUNCTION
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# TIME FUNCTIONS
def time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("THE CURRENT TIME IS : " + time)

# DATE FUNCTIONS
def date():
    day = datetime.datetime.now().strftime("%A")
    mon = datetime.datetime.now().strftime("%B")
    date = datetime.datetime.now().day
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    speak("THE CURRENT DATE IS : " + str(date) + str(month) + str(year))
    speak("THE RUNNING MONTH IS : " +  mon)
    speak("TODAY IS : " + day)

# TIMEZONE
def timezone():
    date = datetime.date.today()
    speak(str(date))

# HOUR FUNCTIONS
def hour():
    hour = datetime.datetime.now().hour
    good_morning = "HELLO SIR HAVE A GREAT DAY !!! A VERY GOOD MORNING SIR"
    good_afternoon = "GOOD AFTERNOON SIR !!!"
    good_evening = "GOOD EVENING SIR !!! HAVE A PLEASNT EVENING"
    good_night = "GOOD NIGHT, SWEET DREAMS, TAKE CARE, HAVE A TIGHT SLEEP SIR"
    if hour >= 6 and hour < 12:
        speak(good_morning)
    elif hour >= 12 and hour < 18:
        speak(good_afternoon)
    elif hour >= 18 and hour < 22:
        speak(good_evening)
    else:
        speak(good_night)

# GREETING ME FUNCTIONS
def wishme():
    wish = "HELLO JAI"
    speak(wish)
    hour()
    time()
    date()
    timezone()
    speak("JAI'S PERSONAL ASSISTANCE IS HERE. HOW MAY I HELP YOU")

# TAKING COMMAND FUNCTIONS
def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("LISTENING...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        speak("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(query)
        speak(query)
        
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query

def google():
    speak("What should I search?")
    Search_term = TakeCommand().lower()
    wb.open('https://www.google.com/search?q='+Search_term)

# EXIT FUNCTIONS / TERMINATION
def exit():
    speak("TERMINATING THE ASSISTANT")
    quit()

# TESTING

# def utc():
#     date = datetime.datetime.utcnow().hour
#     ind = datetime.datetime.now().hour
#     print(date, ind)

# def country():
#     timeZ_Ce = pytz.timezone('US/Central') 
#     dt_Ce = datetime.datetime.now(timeZ_Ce)
#     date = dt_Ce.strftime("%I:%M")
#     timeZ_Ce2 = pytz.timezone('Asia/Kolkata') 
#     dt_Ce2 = datetime.datetime.now(timeZ_Ce2)
#     date2 = dt_Ce2.strftime("%I:%M")
#     print(date, date2)

# TESTING ENDED


# MAIN BODY

if __name__ == "__main__":
    
    speak("Hello Jai")  #LATER CHANGE TO wishme()

    while True:
        query = TakeCommand().lower()

        if 'exit' in query:
            exit()

        elif query:
            speak("SEARCHNG...")
            # query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)
            wb.open('https://www.google.com/search?q='+query)

        # elif query:
        #     speak("SEARCHING...")
        #     # path = 'https://www.google.com/search?q='+query
        #     wb.open_new_tab(query+".com")

        # elif query:
        #     speak("SEARCHING...")
        #     response = GoogleSearch().search(query)
        #     for result in response.results:
        #         print("Title:" + result.title)
        #         print("Content: " + result.getText())

# EXE FILE
# dist/assistant.exe
# pyinstaller --onefile -w assistant.py
# pyinstaller --onefile -windowed assistant.py
