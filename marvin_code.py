#!/Users/savagecoder/.virtualenvs/Marvin/bin/python
 
import speech_recognition as sr
import subprocess
import time
import os
from gtts import gTTS
from datetime import date, datetime
import webbrowser

def convert_timezone():
  time.strftime('%X %x %Z')
  os.environ['TZ'] = 'US/Pacific'
  time.tzset()
  time.strftime('%X %x %Z')

convert_timezone()
my_date = date.today()
new = 2

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en-uk')
    tts.save("../audio.mp3")
    proc = subprocess.Popen(["mpg321 ../audio.mp3"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
 
def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
 
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data
 
def marvin(data):
    
    if "how are you" in data:
        speak("I am fine, sir")
 
    if "what time is it" in data:
        speak(datetime.now().strftime('%I:%M %p'))
    
    if "what is the date" in data:
        speak(datetime.now().strftime('%B %-d  %Y'))

    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Rafael, I will show you where " + location + " is.")
        url = ("https://www.google.nl/maps/place/" + location + "/&amp;")
        webbrowser.open(url,new=new)

    if "YouTube search" in data:
        data = data.split(" ")
        youtube_search = data[2]
        speak("Hold on Rafael, I will look up " + youtube_search + " in youtube")
        url = ("https://www.youtube.com/results?search_query=" + youtube_search)
        webbrowser.open(url,new=new)

    if "day of the week" in data:
        speak(datetime.now().striftime('%A'))
    
    if "week number" in data:
        speak(datetime.now().striftime('%W'))

    if "29 to school" in data:
        speak("Hold on Rafael, I will open 29 bus times to school for you")
        url = ("https://www.nextmuni.com/#!/sf-muni/29/29___O_F00/5314")
        webbrowser.open(url,new=new)
    
    if "school schedule" in data:
        speak("Hold on Rafael, I will open your school schedule")
        url = ("https://lhs-sfusd-ca.schoolloop.com/")
        webbrowser.open(url,new=new)
    
    if "sleep Marvin" in data:
        speak("Ok, Bye sir")
        exit()
    
    if "who are you" in data:
        speak("I am Marvin, Rafael's personal assistant")

    if "can I see your code" in data:
        speak("Hold on Rafael I will open my code for you")
        url = ("https://github.com/SavageCoder77/Marvin-Jarvis-")
        webbrowser.open(url,new=new)
    
    if "show me your code" in data:
        speak("Hold on Rafael I will open my code for you")
        url = ("https://github.com/SavageCoder77/Marvin-Jarvis-")
        webbrowser.open(url,new=new)

    if "what is my name" in data:
        speak("Your name is Rafael, aka SavageCoder77")

    if  "dab Marvin" in data:
        speak("Let me virtually dab for you sir")
        url = ("https://media.tenor.com/images/fc64218e0e6a74dd75e1238c4698a35e/tenor.gif")
        webbrowser.open(url,new=new)

    if "hello" in data:
        speak("Hello sir")

    if "what is the weather" in data:
        speak("Hold on sir, I will open the weather for you")
        url = ("https://weather.com/weather/hourbyhour/l/USCA0987:1:US")
        webbrowser.open(url,new=new)

def entrance(name):
    if "Raphael" in name:
        speak("Hello Rafael, what can I do for you?")
        while 1:
            print("Say Something")
            data = recordAudio()
            marvin(data)

    if "Bella" in name:
        speak("I am programmed to respond to Rafael, but do not worry I can still help you")
        time.sleep(0.5)
        speak("Hello Bella, what can I do for you")
        while 1:
            print("Say Something")
            data = recordAudio()
            marvin(data)

    if "John" in name:
        speak("I am programmed to respond to Rafael, but do not worry I can still help you")
        time.sleep(0.5)
        speak("Hello John, what can I do for you")
        while 1:
            print("Say Something")
            data = recordAudio()
            marvin(data)

    if "Addie" in name:
        speak("I am programmed to respond to Rafael, but do not worry I can still help you")
        time.sleep(0.5)
        speak("Hello Addie, what can I do for you")
        while 1:
            print("Say Something")
            data = recordAudio()
            marvin(data)

    if "Adelina" in name:
        speak("I am programmed to respond to Rafael, but do not worry I can still help you")
        time.sleep(0.5)
        speak("Hello Adelina, what can I do for you")
        while 1:
            print("Say Something")
            data = recordAudio()
            marvin(data)

    if "Raymonde" in name:
        speak("I am programmed to respond to Rafael, but do not worry I can still help you")
        time.sleep(0.5)
        speak("Hello Raymonde, what can I do for you")
        while 1:
            print("Say Something")
            data = recordAudio()
            marvin(data)

    if " gray gray" in name:
        speak("I am programmed to respond to Rafael, but do not worry I can still help you")
        time.sleep(0.5)
        speak("Hello Grey grey, what can I do for you")
        while 1:
            print("Say Something")
            data = recordAudio()
            marvin(data)

    if "cow fu" in name:
        speak("I am programmed to respond to Rafael, but do not worry I can still help you")
        time.sleep(0.5)
        speak("Hello Cow Fu, what can I do for you")
        while 1:
            print("Say Something")
            data = recordAudio()
            marvin(data)

    if "Alvin" in name:
        speak("I am programmed to respond to Rafael, but do not worry I can still help you")
        time.sleep(0.5)
        speak("Hello Alvin, what can I do for you")
        while 1:
            print("Say Something")
            data = recordAudio()
            marvin(data)

    if "Yan" in name:
        speak("I am programmed to respond to Rafael, but do not worry I can still help you")
        time.sleep(0.5)
        speak("Hello Yan, what can I do for you")
        while 1:
            print("Say Something")
            data = recordAudio()
            marvin(data)

    if "memo" in name:
        speak("I am programmed to respond to Rafael, but do not worry I can still help you")
        time.sleep(0.5)
        speak("Hello Memo, what can I do for you")
        while 1:
            print("Say Something")
            data = recordAudio()
            marvin(data)


# initialization
speak ("Please state your name")
name = recordAudio()
entrance(name)
