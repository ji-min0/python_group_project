import json
import random

# JSON에서 대체어 불러오기
with open("tone_dict.json", "r", encoding="utf-8") as f:
    replacement_dict = json.load(f)

def filter_text(text):
    for bad_word, replacements in replacement_dict.items():
        if bad_word in text:
            text = text.replace(bad_word, random.choice(replacements))
    return text
