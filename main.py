from filter import filter_text
from stats import save_log, show_stats

def main():
    print("🐹 귀여운 욕설 차단기 시작! (quit 입력 시 종료)\n")

    while True:
        text = input("💬 변환할 문장을 입력하세요 (엔터 또는 quit 입력 시 종료): ")

        # 종료 조건
        if text.strip() == "" or text.lower() == "quit":
            print("\n📊 프로그램을 종료합니다. 아래에서 기록을 확인하세요!\n")
            break

        # 욕 변환 실행
        result = filter_text(text)

        # 원본 + 변환 결과 출력
        print("\n--- 변환 결과 ---")
        print(f"원본 : {text}")
        print(f"변환 : {result} 💖")
        print("----------------\n")

        save_log(text, result)

    # 통계 출력 (욕 횟수, Top5 등은 stats.py에서 담당)
    show_stats()

if __name__ == "__main__":
    main()
