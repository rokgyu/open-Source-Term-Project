# model_loader.py

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def load_model(model_name):
    tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-ko-en")
    model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-ko-en")
    return tokenizer, model
