# IMPORT LIBRARIES

import pyttsx3  #pip install pyttsx3 
import speech_recognition as sr  #pip install SpeechRecognition
import pytz  #pip install pytz
import wikipedia  #pip install wikipedia
import psutil  #pip install psutil
import pyjokes #pip install pyjokes
import pyautogui  #pip install pyautogui
import wolframalpha  #pip install wolframalpha
import winshell  #pip install winshell

import datetime
import webbrowser as wb
import smtplib
import time
import os
import json
from urllib.request import urlopen
import requests
import random
import operator

# FUNCTIONS

assistant_name_male = "NARUTO"
assistant_name_female = "MIKASA"

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # UPDATION REQUIRED

wolframaplha_app_id = 'Q798R2-7X3639JUX7'

# SPEAK FUNCTION
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# TIME FUNCTIONS
def time_():
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
    speak("TODAY IS : " + str(date))

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
    time_()
    date()
    timezone()
    speak("JAI'S PERSONAL ASSISTANCE 'NARUTO' IS HERE. HOW MAY I HELP YOU")

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

# LATER PURPOSE
# def wiki():
#     speak("SEARCHING...")
#     # query = replace("wikipedia", "")
#     result = wikipedia.summary(query, sentences=2)
#     speak("According to Wikipedia")
#     print(result)
#     speak(result)
# ENDED LATER PURPOSE

# SMPT SERVER
def sendEmail(to, content):
    server = smtplib.SMTP('jaidoshi18.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail 
    server.login('Your email', 'Your password')
    server.sendmail('jaidoshi18@gmail.com', to, content)
    server.close()

# EMAIL FUNCTION
def email():
    try:
        speak("WHAT SHOULD I SAY ??")
        content = TakeCommand()
        speak("WHO IS THE RECEIVER ??")
        receipt = input("ENTER THE NAME OF RECEIPTANT")
        to = (receipt)
        sendEmail(to,content)
        speak(content)
        speak("EMIAL HAS BEEN SENT !!!")
    except Exception as e:
        print(e)
        speak("UNABLE TO SEND EMAIL !!!")

# CHROME SEARCH
def chrome():
    speak("WHAT SHOULD I SEARCH ??")
    path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    search = TakeCommand().lower()
    wb.get(path).open_new_tab(search + ".com")

# YOUTUBE SEARCH
def youtube():
    speak("What should I search?")
    Search_term = TakeCommand().lower()
    speak("Here we go to Youtube\n")
    wb.open("https://www.youtube.com/results?search_query="+Search_term)
    time.sleep(5)

# GOOGLE SEARCH
def google():
    speak("What should I search?")
    Search_term = TakeCommand().lower()
    wb.open('https://www.google.com/search?q='+Search_term)

# CPU FUNCTION
def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU IS AT : " + usage)
    battery = psutil.sensors_battery()
    speak("BATTERY IS AT : " + str(battery.percent) + "%")

# JOKE FUNCTION
def jokes():
    joke = pyjokes.get_joke()
    speak(joke)

# OPENING MS WORD
def word():
    speak("OPENING MICROSOFT WORD...")
    ms_word = r'C:\Program Files\WindowsApps\Microsoft.Office.Desktop.Word_16040.10730.20103.0_x86__8wekyb3d8bbwe\Office16\WINWORD.exe'
    os.startfile(ms_word)

# NOTES SESSION   #UPDATION REQUIRED
## WRITING NOTES
def write():
    speak("WHAT SHOULD I SPEAK ??")
    notes = TakeCommand()
    file = open('notes.txt', 'w')
    speak("WANT TO ADD DATE AND TIME.")
    answer = TakeCommand()
    if answer == 'yes' or answer == 'sure':
        date_time = datetime.datetime.now().strftime("%H:%M:%S")
        file.write(date_time)
        file.write(" :- ")
        file.write(notes)
        speak("NOTES DONE !!! INCLUDING DATE TIME")
    else:
        file.write(notes)
        speak("NOTES DONE !!!")
## READING NOTES
def read():
    speak("SHOWING NOTES...")
    file = open("notes.txt", 'r')
    print(file.read())
    speak(file.read())

# SCREENSHOT FUNCTION   #UPDATION REQUIRED
def screenshot():
    img = pyautogui.screenshot()
    img.save(r"C:\Users\Jai\OneDrive\Desktop\Jai's Assistant\images\ss.png")
    speak("SCREENSHOT HAS BEEN SAVED !!!")

# REMEMBER FUNCTION   # DELETION / UPDATION REQUIRED
def remember():
    speak("WHAT SHOULD I REMEMBER ??")
    memory = TakeCommand()
    speak("I HAD REMEMBERED : " + memory)
    remember_me = memory
    return remember_me

def remember_():
    remembered = remember()
    speak(remembered)

# IMAGE FUNCTIONS   #UPDATION REQUIRED
def image():
    speak("WHICH IMAGE YOU WANT TO VIEW ??")
    # format = TakeCommand()
    name = TakeCommand()
    path = r"C:\Users\Jai\OneDrive\Pictures\Saved Pictures" + name
    speak("OPENING : " + name)
    os.startfile(path)

# NEWS FUNCTIONS   # UPDATION REQUIRED
def news():
    try:
        jsonObj = urlopen('http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=1de284fbf353477387b71921aed4847b')
        data = json.load(jsonObj)
        i = 1

        speak("SOME OF THE TOP HEADLINES OF INDIA")
        print("============= TOP HEADLINES =============")

        for item in data['articles']:
            print(str(i) + '. '  + item['title'] + '\n')
            print(item['description'] + '\n')
            speak(str(i) + '. '  + item['title'] + '\n')
            i += 1

    except Exception as e:
        print(str(e))

# LOCATION FUNCTIONS   # UPDATION REQUIRED
def location():
    speak("WHICH PLACE DO YOU WANT TO BE FOUND ??")
    answer = TakeCommand()
    location = answer
    wb.open("https://www.google.com/maps/place/" + location + "")

# WEATHER FUNCTION   # UPDATION REQUIRED
def weather():
    api_key = "f53ce8408c1cc44b1a2683772535d1c5"
    base_url = "http://api.openweathermap.org/data /2.5/weather?q="
    speak(" City name ")
    print("City name : ")
    city_name = TakeCommand()
    complete_url = base_url + "appid =" + api_key + "&q =" + city_name
    response = requests.get(complete_url)
    x = response.json()
            
    if x["cod"] != "404":
        y = x['main']
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
                
    else:
        speak(" City Not Found ") 

# PROJECT FUNCTION   # UPDATION REQUIRED

# FRIENDS FUNCTION   # UPDATION REQUIRED
def friend():
    speak("TELL ME THE LAST DIGIT OF YOUR MOBILE NUMBER")
    ans = TakeCommand()
    answer = int(ans)
    if answer == 10:
        os.startfile(r"C:\Users\Jai\OneDrive\Pictures\Saved Pictures\jai.jpg")
        os.startfile(r"C:\Users\Jai\OneDrive\Desktop\Jai's Assistant\mp3\testing.mp3")

# CALCULATE FUNCTION  # UPDATION REQUIRED
# def calculate():
#     app_id = 'Q798R2-7X3639JUX7'

# PLAY SONGS FUNCTION
# def songs():
#     songs_path = r"C:\Users\Jai\OneDrive\Desktop\Jai's Assistant\songs"
#     video_path = r"C:\Users\Jai\OneDrive\Desktop\Jai's Assistant\videos"

#     speak("WHAT KIND OF SONGS WOULD YOU LIKE TO LISTEN ?? AUDIO OR VIDEO")
#     answer = TakeCommand().lower()

#     while(answer != 'audio' and answer != 'video'):
#         speak("ENABLE TO RECOGNISE !! PLEASE REPEAT IT AGAIN")
#         answer = TakeCommand().lower()

#     if answer == 'audio':
#         songs_dir = songs_path
#         songs = os.listdir(songs_dir)
#         print(songs)
#     elif answer == 'video':
#         video_dir = video_path
#         songs = os.listdir(video_dir)
#         print(songs)

#     speak("SELECT A RANDOM NUMBER !!!")
#     rand = TakeCommand().lower()

#     while(rand == 'number' and rand == 'random'):
#         speak("DID NOT RECOGNIZED !!! SAY THAT AGAIN")
#         rand = TakeCommand().lower()

#     if rand == 'number':
#         rand = int(rand.replace("number", ""))
#         os.startfile(os.path.join(songs_dir, songs[rand]))
#         continue

#     elif rand == 'random':
#         rand = random.randint(1, 20)
#         os.startfile(os.path.join(songs_dir, songs[rand]))
#         continue

# INTRODUCTION FUNCTION
def Introduction():
    speak("I am NARUTO , Personal AI assistant , "
    "I am created by JAI , "
    "I can help you in various regards , "
    "I can search for you on the Internet , "
    "I can also grab definitions for you from wikipedia , "
    "In layman terms , I can try to make your life a bed of roses , "
    "Where you just have to command me , and I will do it for you , ")

# CREATOR INFO FUNCTION
def Creator():
    speak("JAI is an extra-ordinary person ,"
    "He has a passion for Robotics, Artificial Intelligence and Machine Learning ,"
    "He is very co-operative ,"
    "If you are facing any problem regarding the 'NARUTO', He will be glad to help you ")

# EMPTY RECYCLEBIN FUNCTION
def recyclebin():
    winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
    speak("Recycle Bin Recycled")

# CLEAR FUNCTION   # UPDATION REQUIRED
def clear():
    os.system('cls')
    speak("CLEARED THE TERMINAL FOR YOU SIR !!!")

# SLEEP FUNCTION   # UPDATION REQUIRED
# LOGOUT FUNCTION
def logout():
    os.system("shutdown -l")
# RESART FUNCTION
def restart():
    os.system("shutdown /r /t 1")
# SHUTDOWN FUNCTION
def shutdown():
    os.system("shutdown /s /t 1")

# PAUSE FUNCTION / HAULT
def pause():
    speak("HOW MANY SECONDS YOU WANT ASSISTANT TO BE PAUSE...")
    sec = int(TakeCommand())
    speak("ASSISTANT WILL NOT LISTEN UNTIL " + str(sec) + "seconds")
    time.sleep(sec)
    speak("ASSISTANT HAVE BEEN STARTED AFTER : " + str(sec) + "secounds")

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

    wishme()

    clear()
    
    # speak("Hello Jai")  #LATER CHANGE TO wishme()

    while True:
        query = TakeCommand().lower()

        if 'time' in query:
            time_()
        
        elif 'date' in query:
            date()

        elif 'today' in query:
            timezone()

        # TESTING CONDITION
        # elif query:
        #     wb.open('https://www.google.com/search?q='+query)

        # elif 'new' in query:
        #     url = 'https://openweathermap.org/find?q='
        #     city = 'mumbai'
        #     wb.open(url+city)
        # ENDED TESTING CONDITION

        # UPDATION TESTING REQUIRED
        elif 'tell me about yourself' and 'who are you' in query:
            Introduction()

        elif 'tell me about jai' and 'creator' in query:
            Creator()

        elif 'how are you' in query:
            speak("I am fine, Sir Thanks for asking")
            speak("How are you Sir?")
            if 'fine' in query or "good" in query: 
                speak("It's good to know that your fine")
            else:
                speak("I hope you get well soon.")

        elif "who am i" in query:
            speak("If you can talk, then definitely you are a human")

        elif "why you came to this world" in query:
            speak("Thanks to JAI. further it is a secret")

        elif 'what is love' and 'tell me about love' in query:
            speak("It is 7th sense that destroy all other senses , "
            "And I think it is just a mere illusion , "
            "It is waste of time")

        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")
            
        elif "i love you" in query:
            speak("It's hard to understand, I am still trying to figure this out.")
        # UPDATION TESTING REQUIRED

        elif 'wikipedia' in query:  #CHANGES REQUIRED
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)

        elif 'send email' in query:
            email()

        elif 'search in chrome' in query:
            chrome()

        elif 'open youtube' in query:
            youtube()

        elif 'search google' in query:
            google()

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()

        elif 'word' in query:
            word()

        elif 'write notes' in query:
            write()

        elif 'read notes' in query:
            read()

        elif 'screenshot' in query:
            screenshot()

        elif 'remember that' in query:
            remember()

        elif 'do you remember anything' in query:
            remember_()

        elif 'open image' in query:
            image()

        elif 'news' in query:
            news()

        elif 'find location' in query:
            location()

        elif 'weather' in query:
            weather()

        elif 'calculate' in query:
            client = wolframalpha.Client(wolframaplha_app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif 'what is' in query or 'who is' in query:   # HIGH LEVEL UPDATION REQUIRED
            client = wolframalpha.Client(wolframaplha_app_id)
            res = client.query(query)
            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("NO RESULT")
                speak("NO RESULT")

        elif 'play songs' in query:   # HUGE UPDATION REQUIRED
            video = r"C:\Users\Jai\OneDrive\Desktop\Jai's Assistant\videos"
            audio = r"C:\Users\Jai\OneDrive\Desktop\Jai's Assistant\songs"
            speak("What songs should i play? Audio or Video")
            ans = (TakeCommand().lower())
            while(ans != 'audio' and ans != 'video'):
                speak("I could not understand you. Please Try again.")
                ans = (TakeCommand().lower())
        
            if 'audio' in ans:
                    songs_dir = audio
                    songs = os.listdir(songs_dir)
                    print(songs)
            elif 'video' in ans:
                    songs_dir = video
                    songs = os.listdir(songs_dir)
                    print(songs)
                
            speak("select a random number")
            rand = (TakeCommand().lower())
            while('number' not in rand and rand != 'random'):                       
                speak("I could not understand you. Please Try again.")          
                rand = (TakeCommand().lower())

            if 'number' in rand:
                    rand = int(rand.replace("number ",""))
                    os.startfile(os.path.join(songs_dir,songs[rand]))
                    continue                                              
            elif 'random' in rand:
                    rand = random.randint(0, 1)
                    os.startfile(os.path.join(songs_dir,songs[rand]))
                    continue

        elif 'friend' in query:
            friend()

        elif 'empty recycle bin' in query:
            recyclebin()

        elif 'logout' in query:
            logout()

        elif 'restart' in query:
            restart()

        elif 'shutdown' in query:
            shutdown()

        elif 'pause' in query:
            pause()

        elif 'exit' in query:
            exit()

