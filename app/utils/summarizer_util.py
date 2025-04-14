# app/utils/summarizer_utils.py
from summarizer import Summarizer

model = Summarizer(model="bert-base-uncased")

def generate_summary(text, ratio=0.2):
    return model(text, ratio=ratio)
