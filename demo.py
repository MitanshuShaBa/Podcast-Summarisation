import streamlit as st

import os
os.environ['TRANSFORMERS_CACHE'] = 'experiments/cache_dir/'

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM  

st.title('Podcast Summarization Demo')
tokenizer = AutoTokenizer.from_pretrained("knkarthick/bart-large-xsum-samsum")
model = AutoModelForSeq2SeqLM.from_pretrained("knkarthick/bart-large-xsum-samsum")

text = st.text_area('Text Input')

def run_model(input_text):
    tokens = tokenizer(input_text, truncation=True, padding="longest", return_tensors="pt")
    summary = model.generate(**tokens)
    output_text = tokenizer.decode(summary[0], skip_special_tokens=True, clean_up_tokenization_spaces=False)
    st.write('Summary')
    st.success(output_text)


if st.button('Submit'):
    run_model(text)