import json
import random

def load_profanity_list(): 
    """
    profanity.json 파일 읽어옴
    문제가 있을 경우 빈 리스트 반환
    """
    try: 
        with open("profanity.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            
            #list가 아님
            if not isinstance(data, list):
                raise TypeError("⚠️ JSON 데이터가 리스트가 아닙니다 ⚠️")
            return data
    # 파일이 없음
    except FileNotFoundError:
        print("⚠️ profanity.json 파일을 찾을 수 없습니다.")
        return []
    # 디코딩 실패
    except json.JSONDecodeError:
        print("⚠️ JSON 디코딩 실패: 파일이 깨졌거나 올바른 형식이 아닙니다.")
        return []
    
    except TypeError as e:
        print(e)
        return []

# 필터링한 단어 10개(대체어) 목록
def load_replacement_words():
    return[
        "유니콘🦄", "무지개🌈", "햇살🔆", "꽃🌻", "별✨", 
        "사랑💖", "희망🌱", "비눗방울🫧", "바다🌊", "숲🌳"
        ]

def filter_profanity(text: str) -> str: 
    """
    욕설을 필터링하고 랜덤 대체어로 바꿔줌
    """
    profanity_list = load_profanity_list()
    replacement_words = load_replacement_words()
    
    # 텍스트에 포함된 욕설을 랜덤 대체어로 변환
    for swear in profanity_list: 
        if swear in text: 
            text = text.replace(swear, random.choice(replacement_words))
            
    return text
