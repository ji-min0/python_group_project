import json
import random

# JSON에서 대체어 불러오기
with open("tone_dict.json", "r", encoding="utf-8") as f:
    replacement_dict = json.load(f)

def filter_text(text):
    # 톤 선택 제거 → 기본 하나의 dict만 사용
    tone_dict = replacement_dict.get("cute", {})
    for bad_word, replacements in tone_dict.items():
        if bad_word in text:
            text = text.replace(bad_word, random.choice(replacements))
    return text