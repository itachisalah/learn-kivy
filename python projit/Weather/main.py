import pyttsx3
import speech_recognition as sr

wel = pyttsx3.init()
voices = wel.getProperty('voices')
wel.setProperty('voices', voices [0].id)

def Speak(audio):
    wel.say(audio)
    wel.runAndWait()
def TakeCommands():
    command = sr.Recognizer()
    with sr.Microphone() as mic :
        print('Say commands sir ....')
        command.phrase_threshold =1
        audio = command.listen(mic)
        try:
            print('Recording...')
            query = command.recognize_google(audio, language='en')
            print(f'you said :{query}')
        except Exception as Error:
            return None
        return query.lower()


Speak('Hello sir Salaheddine , say your commands please')
TakeCommands()

