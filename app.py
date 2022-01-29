import streamlit as st
import transformers
import os
# import speech_recognition as sr
# from gtts import gTTS
# import os
# import playsound

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM  

@st.cache
def load_model():
    model = AutoModelForSeq2SeqLM.from_pretrained(os.path.join(os.curdir, "models", "bart-large-xsum-samsum"))
    return model

tokenizer = AutoTokenizer.from_pretrained(os.path.join(os.curdir, "tokenizers", "bart-large-xsum-samsum"))
model = load_model()

# def speak(text):
#     tts = gTTS(text=text, lang='en')
#     filename = 'voice.mp3'
#     tts.save(filename)
#     playsound.playsound(filename)
#     os.remove('voice.mp3')

@st.cache
def get_tokens(text):
    tokens = tokenizer(text, truncation=True, padding="longest", return_tensors="pt")
    return tokens

def infer(tokens):
    summary = model.generate(**tokens)
    output = tokenizer.decode(summary[0])
    return output

st.title("Podcast Summarisation 🦄")
