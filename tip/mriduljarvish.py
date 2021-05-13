import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine=pyttsx3.init()
voices=engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
      speak("Good Morning! Maam")
    elif(hour>=12 and hour<18):
      speak("Good Afternoon! Maam")
    else:
      speak("Good Evening! Maam")
    speak("Hi I am Your Personal Assistent Please tell me how I may help you")

def takecommand():
      # take microphone input from the user and return string output...
      r=sr.Recognizer()
      with sr.Microphone() as source:
            print("Listening...........")
            r.pause_threshold=1
            audio=r.listen(source)
      try:
            print("Recognizing....")
            query=r.recognize_google(audio,language="en-in")
            print(f"user said:",(query),"\n")
      except Exception as e:
            speak("Say that again Please.....")
            return "None"
      return query
if __name__=="__main__":
    wishMe()
    query=takecommand().lower()
    list1=["play a music","play a song","play music","play song","music","song"]
    list2=["open tip calculator","tip calculator"]
    if "wikipedia" in query:
        speak("Searching wikipedia Please wait")
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=5)
        speak("According to wikipedia")
        print(results)
        speak(results)
    elif "open youtube" in query:
        webbrowser.open("youtube.com")
    elif "open google" in query:
        webbrowser.open("google.com")
    elif "open stackoverflow" in query:
        webbrowser.open("stackoverflow.com")

    elif ((list1[0] in query)or(list1[1] in query) or(list1[2] in query)or(list1[3] in query)or(list1[4] in query)or(list1[5] in query)):
        music_dir="F:\\New folder"
        songs=os.listdir(music_dir)
        print(songs)
        mr=random.randint(0,len(songs))
        os.startfile(os.path.join(music_dir,songs[mr]))
    elif "the time" in query:
        strTime= datetime.datetime.now().strftime("%H:%M:%S")
        speak(f" Maam The time is {strTime}")
    elif (("the date" in query) or("date" in query)):
        f1=["januay"," february","march","april","may","june","july","august","september","october","november","december"]
        strDate= datetime.datetime.today().date()
        speak(f" Maam The date is {strDate.day} {f1[(strDate.month)-1]} {strDate.year}")
    elif ((list2[0] in query)or(list2[1] in query)):
        speak("Please wait Maam")
        codePath="C://Users//LENOVO//Desktop//tip//index.html"
        os.startfile(codePath)
