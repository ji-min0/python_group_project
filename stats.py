import datetime
from collections import Counter

# 로그 파일 이름 정의
log_file = "logs.txt"


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
    
    with open(log_file, "a", encoding="utf-8") as f: 
        # 로그 포맷: [시간] 입력: ... -> 결과: ...
        f.write(f"[{timestamp}] 입력: {user_input} -> 변환 결과: {filtered_output}\n")


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
    filtered_count = sum(1 for log in logs if "감지된 욕설:" in log and log.split("감지된 욕설:")[1].split(", 변환 결과:")[0].strip() != "없음")

    # 결과 문장에서 단어별 등장 빈도 계산
    words = []
    for log in logs: 
        if "감지된 욕설:" in log: 
            filtered = log.split("-> 변환 결과:")[1].strip()

            # 변환 결과가 있으면
            if filtered: 
                words.extend(filtered.replace(","," ").split())
    
    common_words = Counter(words).most_common(5)
    
    return {
        "총 입력 수": total_inputs,
        "욕설 사용 문장 수": filtered_count,
        "가장 많이 나온 단어 Top 5": common_words
    }


def give_praise(stats: dict) -> None:
    """
    통계를 보고 욕을 적게 썼으면 칭찬 메시지 출력
    """
    filtered_count = stats.get("욕설 사용 문장 수", 0)
    
    if filtered_count == 0:
        print("바르고 고운 말만 사용했어요! 칭찬해요 💖")
    elif filtered_count < 3: 
        print("욕설을 조금만 사용했어요! 앞으로도 응원해요 🐹")
    else: 
        print("욕이 조금 많았어요ㅠㅠ 더 조심히 말해보아요! 💪")
