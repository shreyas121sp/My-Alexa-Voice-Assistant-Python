import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
engine.say("iam your alexa")
engine.say("what can i do for you")
engine.runAndWait()
def talk(text):
    engine.say(text)
    print(text)
    engine.runAndWait()

def take_command():
    command =" "
    try:
        with sr.Microphone() as source:

            print("listening.....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                talk(command)
                command = command.replace('alexa','')
                
    except:
        pass 
    return command

def run_alexa():
    command = take_command() 
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)   

    elif 'time' in command: 
        time = datetime.datetime.now().strftime('%I:%M %p') 
        talk('curent time is '+ time)  

    elif 'tell me about' in command:
        person = command.replace('tell me about','')
        info = wikipedia.summary(person,3)
        print(person)
        talk(info)      

run_alexa()        