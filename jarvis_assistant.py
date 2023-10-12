
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening") 



def takeCommand():
    #It takes microphone input from the user and returns string output
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio2 = r.listen(source)

    try:
        print("Recognizing....")
        query=r.recognize_google(audio2,language='en_in')
        print(f"user said: {query}\n")
    except Exception as e:
        #print(e)
        print(" Say that again please...")
        return "None"

    return query
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('kemdarneaditya008@gmail.com' ,'Adityaraj')
    server.sendEmail('kemdarneaditya008@gmail.com',to,content)
    server.close()

speak("Hi,I am Jarvis. Sir, Please tell me how may I help you")        
if __name__ == "__main__":
    wishMe()

    while True:
        query=takeCommand().lower()
       # print(mytext.lower())


    # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak ('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=5)
            speak("According to Wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open spotify' in query:
            webbrowser.open("spotify.com")
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
            
        elif 'play music' in query:
            music_dir 
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'What is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\Lenovo\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(codepath)
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Aditya.") 
        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
                        
        elif ' email to aditya' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to   = "adityayouremail@gmail.com"  
                sendEmail(to,content)
                speak("Email has been sent")

            except Exception as e:
                print(e)
                speak("Sorry my friend aditya bhai. I am not able to send this email") 

        elif "temperature" in query:

            search = "temperature in pune"
            url = f"http://www.google.com/search?q{search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current{search} is {temp}")
        elif "weather" in query:
             
            # Google Open weather website
            # to get API of Open weather
            api_key = "Api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" Pune ")
            print("Pune : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name

            response = requests.get(complete_url)
            x = response.json()
             
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
        elif "where is Pune" in query:
            query = query.replace("where is", "Pune")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")
 
           
           




       
       
   


                    








