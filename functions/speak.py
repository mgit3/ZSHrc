from gtts import gTTS
import os
import time
import playsound

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = '.voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)



stop = False
while stop ==  False:
    text = input('Paste the text:   ')
    speak(text)

