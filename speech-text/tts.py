from gtts import gTTS
import os

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'summary.mp3'
    tts.save(filename)


with open("summary.txt") as f:
    text = f.read()

speak(text)