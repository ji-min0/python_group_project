import datetime
import json
import random
from collections import Counter

# 로그 파일 이름 정의
log_file = "logs.txt"

# 욕설 키워드 + 변환 단어 리스트 JSON 파일
swear_json = "tone_dict.json"

#json 불러오기
try: 
    with open(swear_json, "r", encoding="utf-8") as f: 
        swear_dict = json.load(f)
        
    # 데이터타입(자료형)이 dict가 아닐 때
    if not isinstance(swear_dict, dict): 
        raise TypeError("⚠️ JSON 데이터가 딕셔너리가 아닙니다 ⚠️")
    
# 파일이 없을 때
except FileNotFoundError: 
    swear_dict = {}
    print("⚠️ 욕설 사전을 찾을 수 없습니다 ⚠️")

# 디코딩 문제(파일 깨졌을 때)
except json.JSONDecodeError: 
    swear_dict = {}
    print("⚠️ JSON 디코딩을 실패했습니다 ⚠️")

# 데이터타입(자료형) 오류
except TypeError as e:
    swear_dict = {}
    print(e)


def convert_swear(text: str) -> str: 
    """
    욕설 단어를 랜덤한 귀여운 단어로 변환하는 함수
    """
    for swear, replacements in swear_dict.items(): 
        if swear in text: 
            text = text.replace(swear, random.choice(replacements))
    return text


def log_event(user_input: str, filtered_output: str) -> None: 
    """
    사용자 입력과 변환 결과를 logs.txt에 저장하는 함수
    파라미터:
        user_input: 사용자가 입력한 원문
        filtered_output: 욕설 변환 후 결과
    파일에 기록될 때는 시간까지 함께 기록
    """
    # 현재 시간 문자열 생성 (예: 2025-08-29 14:35:21)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 원문 욕설 단어 추출
    found_swears = [sw for sw in swear_dict.keys() if sw in user_input]
    found_swears_str = ", ".join(found_swears) if found_swears else "없음"
    
    with open(log_file, "a", encoding="utf-8") as f: 
        # 로그 포맷: [시간] 입력: ... -> 결과: ...
        f.write(f"[{timestamp}] 입력: {user_input} -> 감지된 욕설: {found_swears_str}, 변환 결과: {filtered_output}\n")


def read_logs() -> list[str]: 
    """
    logs.txt 파일을 읽어서 각 줄을 리스트로 반환하는 함수
    로그 파일이 없으면 빈 리스트 반환
    """
    try: 
        with open(log_file, "r", encoding="utf-8") as f: 
            return f.readlines()
    except FileNotFoundError: 
        # 로그 파일이 없으면 빈 리스트 반환
        return []


def analyze_logs() -> dict: 
    """
    로그 파일을 분석해서 간단한 통계를 반환하는 함수
    반환값 예시:
        - 총 입력 수
        - 욕설(치환된 단어) 사용 수
        - 가장 많이 나온 단어 TOP5
    """
    # 로그 불러오기
    logs = read_logs()
    # 총 입력 수 계산
    total_inputs = len(logs)
    
    # 욕 사용 문장 수 계산
    swear_count = sum(1 for log in logs if "감지된 욕설:" in log and log.split("감지된 욕설:")[1].split(", 변환 결과:")[0].strip() != "없음")

    # 결과 문장에서 단어별 등장 빈도 계산
    words = []
    for log in logs: 
        if "감지된 욕설:" in log: 
            sw_text = log.split("감지된 욕설:")[1].split(", 변환 결과:")[0].strip()
            if sw_text != "없음": 
                words.extend(sw_text.split(", "))
    
    common_words = Counter(words).most_common(5)
    
    return {
        "총 입력 수": total_inputs,
        "욕설 사용 문장 수": swear_count,
        "가장 많이 나온 단어 Top 5": common_words
    }


def give_praise(stats: dict) -> None:
    """
    통계를 보고 욕을 적게 썼으면 칭찬 메시지 출력
    """
    swear_count = stats.get("욕설 사용 문장 수", 0)
    
    if swear_count == 0:
        print("바르고 고운 말만 사용했어요! 칭찬해요 💖")
    elif swear_count < 3: 
        print("욕설을 조금만 사용했어요! 앞으로도 응원해요 🐹")
    else: 
        print("욕이 조금 많았어요ㅠㅠ 더 조심히 말해보아요! 💪")

# 테스트
if __name__ == "__main__": 
    # 예시
    user_input = input("문장을 입력하세요: ")
    filtered_output = convert_swear(user_input)
    
    #로그 기록
    log_event(user_input, filtered_output)
    
    # 통계 출력
    stats = analyze_logs()
    print("\n[통계]")
    for k, v in stats.items():
        print(f"- {k}: {v}")
    
    # 칭찬
    give_praise(stats)