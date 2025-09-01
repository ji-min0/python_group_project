import datetime

# 로그 파일 이름 정의
log_file = "logs.txt"


def log_event(user_input: str, filtered_output: str) -> None: 
    """
    사용자 입력과 변환 결과를 logs.txt에 저장하는 함수
    """
    # 현재 시간 문자열 생성 (예: 2025-08-29 14:35:21)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(log_file, "a", encoding="utf-8") as f: 
        # 로그 포맷: [시간] 입력: ... -> 변환 결과: ...
        f.write(f"[{timestamp}] 입력: {user_input} -> 변환 결과: {filtered_output}\n")


def give_praise(filtered_count):
    """
    통계를 보고 욕을 적게 썼으면 칭찬 메시지 출력
    """

    if filtered_count == 0:
        print("바르고 고운 말만 사용했어요! 칭찬해요 💖")
    elif filtered_count < 6: 
        print("욕설을 조금만 사용했어요! 앞으로도 응원해요 🐹")
    else: 
        print("욕이 조금 많았어요ㅠㅠ 더 조심히 말해보아요! 💪")
