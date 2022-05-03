from pydub import AudioSegment 
import speech_recognition as sr
from pathlib import Path
import time

def process(filepath, chunksize=60000):
    #0: load mp3
    sound = AudioSegment.from_mp3(filepath)

    #1: split file into 60s chunks
    def divide_chunks(sound, chunksize):
        # looping till length l
        for i in range(0, len(sound), chunksize):
            yield sound[i:i + chunksize]
    chunks = list(divide_chunks(sound, chunksize))
    print(f"{len(chunks)} chunks of {chunksize/1000}s each")

    r = sr.Recognizer()
    #2: per chunk, save to wav, then read and run through recognize_google()
    string_index = {}
    for index,chunk in enumerate(chunks):
        chunk.export('test.wav', format='wav')
        with sr.AudioFile('test.wav') as source:
            audio = r.record(source)
        s = r.recognize_google(audio, language="en-US")
        print("chunk",index,s)
        string_index[index] = s
        time.sleep(5)
    return string_index

text = process('D:\MyProjects\Python Projects\Podcast-Summarisation\speech-text\sample podcast.mp3')
print(text)

with open("transcript.txt",'w') as f:
    f.write(text)

