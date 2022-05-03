import os
os.environ['TRANSFORMERS_CACHE'] = 'experiments/cache_dir/'

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM  

tokenizer = AutoTokenizer.from_pretrained("knkarthick/bart-large-xsum-samsum")
model = AutoModelForSeq2SeqLM.from_pretrained("knkarthick/bart-large-xsum-samsum")

with open("input.txt") as f:
    text = f.read()

def run_model(input_text):
    tokens = tokenizer(input_text, truncation=True, padding="longest", return_tensors="pt")
    summary = model.generate(**tokens)
    output_text = tokenizer.decode(summary[0], skip_special_tokens=True, clean_up_tokenization_spaces=False)
    print(output_text)
    with open("output.txt", "w") as f:
        f.write(output_text)


run_model(text)