import re

def clean_text(text):
    text = re.sub(r'\n+', ' ', str(text))
    text = re.sub(r'\s+', ' ', text).strip()
    return text
