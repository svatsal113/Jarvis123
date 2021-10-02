import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good morning handsome')
        
    elif hour >= 12 and hour < 16:
        speak('Good afternoon Handsome')
        
    else:
        speak('Good evening Handsome')

    speak('Hello Sir, How may I help you?')   

def takeCommand():
    '''
    it takes microphone input from the user and return string output
    ''' 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.energy_threshold = 300 # minimum audio energy to consider for recording

        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio,language='en-in')
        print(f'User said:{query}\n')
    
    except Exception as e:
        print(e)
        print("Say that again please...")
        return 'None'
    return query



        

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences = 2)
            speak('According to wikipedia')
            speak(results)
        
        elif 'open youtube' in query:
            speak('Opening Youtube...')
            webbrowser.open('https://www.youtube.com/')
        
        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com/")

        elif 'open times of india' in query:
            webbrowser.open("https://timesofindia.indiatimes.com/")

        elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            y = random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir,songs[y]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir the time is {strtime}')


        elif 'quit' in query:
            speak('Good bye sir, we will meet soon')
            break


