
from datetime import datetime

def log_usage(original, filtered):
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] 원본: {original} → 변환: {filtered}\n")

def give_badge():
    print("🎉 오늘도 말 이쁘게 써줘서 고마워요!")