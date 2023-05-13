
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import requests
import json
import webbrowser
import os
import pywhatkit as kit
import smtplib as smt
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
print(voices)
print(rate)
engine.setProperty('rate', 150)
engine.setProperty('voice',voices[1].id)
print(voices[1].id)



author = "Boss"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(f"Good Morning {author}")
    elif hour >= 12 and hour<18:
        speak(f"Good Afternoon {author}")
    else:
        speak(f"Good Evening {author}")

    speak(f"I am your personal Artificial Assistant, Please tell me, how may I help you?")


def takeCommand():
    "take mic input from user and return string"

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1.5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"{author} Said:{query} \n")
    except Exception as e:
        print(f"Sorry {author}, Say that again....")
        return "None"
    return query

if __name__ == "__main__":
    # speak(f"Welcome {author}, I am AI")
    wishMe()
    # takeCommand()

    if 1:
        query = takeCommand().lower()
        if 'wikipedia' and 'who' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak("Acccording to Wikipedia")
            print(results)
            speak(results)

        elif 'news' in query:
            speak("Searching News...")
            query = query.replace("news","")
            url = "https://newsapi.org/v2/top-headlines?country=my&apiKey=c6e0f22304c24cadaf64488757835a00"
            news = requests.get(url).text
            news = json.loads(news)
            art = news['articles']
            for article in art:
                print(article['title'])
                speak(article['title'])

                print(article['description'])
                speak(article['description'])
                speak("Do you want to read more?")
        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")
        
        
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
        
        
        elif 'search browser' in query:
            speak("what should i search?")
            um = takeCommand().lower()
            webbrowser.open(f"{um}")
        
        elif 'ip address' in query:
            ip = requests.get('http://api.ipify.org').text
            print(f"Your ip is {ip}")
            speak(f"Your ip is {ip}")

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'open steam' in query:
            codepath = "C:\\Program Files (x86)\\Steam\\steam.exe"
            os.startfile(codepath)


        elif 'play youtube' in query:
            speak("what should i search in youtube?")
            cm = takeCommand().lower()
            kit.playonyt(f"{cm}")

        elif 'send message' in query:
            speak("who should i send?")
            # num = input("enter number: \n")
            num = takeCommand().lower()
            speak("what should i send?")
            msg = takeCommand().lower()
            speak("please enter time sir.")
            H = int(input("enter hour?\n"))
            M = int(input("enter minutes?\n"))

            kit.sendwhatmsg(num, msg, H, M)

        # elif 'send mail' in query:
        #     speak("what should i send sir?")
        #     content = takeCommand().lower()
        #     speak("whom should i send the mail? enter the mail address sir")
        #     to = input ("enter mail address: \n")
        #     sendmail(to, content)