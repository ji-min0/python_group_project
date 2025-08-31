# main.py
from filter import filter_profanity   # 욕설 변환 함수 (filter.py에 구현)
from stats import log_event, analyze_logs, give_praise

def main():
    print("=== 귀여운 욕 필터기 ===")
    print("종료하려면 'quit' 입력\n")

    while True:
        # 사용자 입력 처리
        text = input("문장을 입력하세요: ")
        
        # 종료조건
        if text.strip() == "" or text.lower() == "quit":
            print("\n프로그램을 종료합니다...\n")
            break

        # 욕설 필터링/변환
        filtered_text = filter_profanity(text)

        # 결과 출력
        print(f"\n[원본] {text}")
        print(f"[변환] {filtered_text}\n")

        # 로그 기록
        log_event(text, filtered_text)

    # 프로그램 종료 후 분석/칭찬
    print("=== 사용 통계 ===")
    stats = analyze_logs()
    give_praise(stats)


if __name__ == "__main__":
    main()