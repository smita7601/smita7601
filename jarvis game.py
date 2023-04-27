import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)


def speak(audio):
    pass
print(voices[0].id)

engine.setProperty('voice',voices[0].id)




def speak(audio):  
    engine .say(audio)
    engine.runAndWait()
    speak("harry is a good boy")

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("i am jarvis Sir. Please tell me how may I help you")

def takecommand() :  
    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold()
         audio = r.listen(source)
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio,language= 'en-in')  
        print(f"user said:{query}\n")


    except Exception as e:
        
        print("say that again please...")
        return "None"
        return query



if __name__=="__main__ " :
    WishMe()
    query = takecommand().lower()




    if 'wikipedia' in query:
        speak("searching wikipedia....")

        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)

        speak('according to wikipedia')
        speak(results)

    elif 'open youtube ' in query:
        webbrowser.open("youtube.com")

    elif 'open google ' in query:
        webbrowser.open("google.com")

    elif 'open chrome ' in query:
        webbrowser.open("chrome.com")


    elif 'open stackoverflow ' in query:
        webbrowser.open("stackoverflow.com")

    


    