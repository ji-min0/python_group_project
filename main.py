from filter import filter_text
from stats import save_log, show_stats

def main():
    print("귀여운 욕설 차단기 시작! (quit 입력 시 종료)")
    tone = "cute"  # 기본값 (나중에 선택 가능하게)

    while True:
        text = input("👉 욕을 입력하세요: ")
        if text.lower() == "quit":
            break
        result = filter_text(text, tone)
        print("💖 변환 결과:", result)
        save_log(text, result)

    show_stats()

if __name__ == "__main__":
    main()
