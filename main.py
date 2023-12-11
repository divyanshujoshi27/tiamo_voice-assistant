import pyttsx3 as p
import speech_recognition as sr
from speech_recognition import audio

engine = p.init()
rate = engine.getProperty('rate')
voices = engine.setProperty('rate',170)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
voices = engine.getProperty('voices')
def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Radhe Radhe DJ ,i am your voice assistant , tiamo ")

r = sr.Recognizer()
# with sr.Microphone() as source:
#     r.energy_threshold=10000
#     r.adjust_for_ambient_noise(source,1.2)
#     audio = r.listen(source)
#     text=r.recognize_google(audio)
#     print(text)//
with sr.Microphone() as source:
    r.energy_threshold = 1000
    r.adjust_for_ambient_noise(source, 1.2)
    print('Listening for 5 seconds...')
   # audio = r.listen(source, timeout=5)
    #print("Audio duration:", len(audio.frame_data) / audio.sample_rate)
    text = r.recognize_google(audio)
    print(text)
if "what" and "about" and "you" in text:
    speak("i am having a good day sir ")
speak("what can i do for you dj")
