# main.py
from filter import filter_text   # 욕설 변환 함수 (filter.py에 구현)
from stats import convert_swear, log_event, analyze_logs, give_praise

def main():
    print("=== 귀여운 욕 필터기 ===")
    print("종료하려면 'quit' 입력\n")

    while True:
        # 2️⃣ 사용자 입력 처리
        text = input("문장을 입력하세요: ")
        
        if text.strip() == "" or text.lower() == "quit":
            print("\n프로그램을 종료합니다...\n")
            break

        # 3️⃣ 욕설 필터링/변환
        filtered_text = convert_swear(filter_text(text))

        # 4️⃣ 결과 출력
        print(f"\n[원본] {text}")
        print(f"[변환] {filtered_text}\n")

        # 5️⃣ 로그 기록
        log_event(text, filtered_text)

    # 6️⃣ 프로그램 종료 후 분석/칭찬
    print("=== 사용 통계 ===")
    analyze_logs()
    give_praise()


if __name__ == "__main__":
    main()

