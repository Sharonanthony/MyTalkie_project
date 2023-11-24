import pyttsx3   
import datetime
import pytz
import speech_recognition as speech
import wikipedia
import webbrowser
import os
import smtplib
from datetime import datetime
import time

engine = pyttsx3.init('sapi5')
rate= engine.getProperty('rate')
engine.setProperty('rate',170)

voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
      hour=int(datetime.now().hour)
      if hour>=0 and hour<12:
            speak("Good morning!")
      elif hour>=12 and hour<18:
            speak("Good afternoon!")
      else:
            speak("Good evening!")
      speak("I am Javaris! How may I help you sir?")

def takeCommand():
      #it takes microphone input from the user and return string output
      r=speech.Recognizer()
      with speech.Microphone() as source:
            print("Listening.....")
            r.pause_threshold= 2
            audio= r.listen(source)

      try:
            print("Recognizing....")
            query=r.recognize_google(audio,language='en-IN')
            print(f"User said: {query}\n" )

      except Exception as e:

            print("Sorry Sir! We couldn't hear you. Can you please say that again")
            return "None"
      return query

def get_system_timezone():
    # Get the local timezone using the system settings
    system_timezone = datetime.now(pytz.timezone('UTC')).astimezone().tzinfo
    return system_timezone

def sendEmail(to,content):
      server= smtplib.SMTP('smtp.gmail.com',587)
      server.ehlo()
      server.starttls()
      server.login("youremail@gmail.com","yourpassword")
      server.sendmail("youremail@gmail.com",to,content)
      server.close()

if __name__== "__main__":
      wishMe()
      #while True:
      if 1:
            query=takeCommand().lower()
            # Logic for executing tasks based on query
            
            if 'wikipedia' in query:
                  speak("Searching Wikipedia....")
                  query=query.replace("wikipedia","")
                  results=wikipedia.summary(query, sentences=2)
                  speak("According to the wikipedia ")
                  print(results)
                  speak(results)
            
            elif 'open youtube' in query:
                  webbrowser.open("youtube.com")
            
            elif 'play music' in query:
                  #create a random module to play randomly
                  music_dir='C:\\Users\\91842\\Desktop\\Music'
                  songs= os.listdir(music_dir)
                  print(songs)
                  os.startfile(os.path.join(music_dir,songs[0]))

            elif 'the time' in query:
                  strTime= datetime.now().strftime("%H:%M:%S") 
                  speak(f"Sir the Time is {strTime}")
            
            elif 'time zone' in query:
                  zone= get_system_timezone()
                  speak(f"The timzone in which you are is {zone}")
            
            elif 'today' in query:
                  strTime= datetime.now().strftime("%H:%M:%S")
                  today_date= datetime.now().date().strftime("%d %B %Y")
                  zone= get_system_timezone()
                  speak(f"Sir today is {today_date}. Currently the time is {strTime} and your time zone is {zone}")
           
            elif 'date' in query:
                  today_date= datetime.now().date().strftime("%d %B %Y")
                  speak(f"Today's date is {today_date}")
            
            elif 'open code' in query:
                  codePath='C:\\Users\\91842\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code'
                  os.startfile(codePath)

            elif 'email to sharon' in query:
                                   
                  try:
                        speak("What should I say?")
                        content= takeCommand()
                        to="xyz@gmail.com"
                        sendEmail(to,content)
                        speak("Email has been sent!")
                  
                  except Exception as e:
                        print(e)
                        speak("Sorry I am unable to send an email")
            
