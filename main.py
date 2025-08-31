from filter import filter_profanity   # 욕설 변환 함수 (filter.py에 구현)
from stats import log_event, give_praise
import os, sys

def main():
    print("=== 귀여운 욕 필터기 ===")
    print("종료하려면 '종료' 입력\n")
    count = 0
    textcount = 0
    while True:
        # 사용자 입력 처리
        text = input("문장을 입력하세요: ")
        
        # 종료조건
        if text.strip() == "" or text.lower() == "종료":
            print("\n프로그램을 종료합니다...\n")
            
            break

        # 욕설 필터링/변환
        filtered_text = filter_profanity(text)

        # 결과 출력
        print(f"\n[원본] {text}")
        print(f"[변환] {filtered_text}\n")
        textcount += 1
        if text != filtered_text:
            count += 1

        # 로그 기록
        log_event(text, filtered_text)

    # 프로그램 종료 후 분석/칭찬
    print("=== 사용 통계 ===")
    print(f"총 입력수 : {textcount}")
    print(f"욕 횟수 : {count}")
    give_praise(count)
    sys.exit()


if __name__ == "__main__":
    while True: 
        print("=== 귀여운 욕 필터기 ===\n")
        print("1. 프로그램 실행")
        print("2. 프로그램 종료")
        print("*. 로그 초기화")

        choice = input("선택하세요 (1, 2, *): ").strip()

        if choice == "1":
            main()  # 기존 프로그램 실행
        elif choice == "2": 
            break
        elif choice == "*":
            # logs.txt 초기화
            if os.path.exists("logs.txt"):
                with open("logs.txt", "w", encoding="utf-8") as f:
                    f.write("")
            print("로그가 초기화되었습니다!")
        else:
            print("잘못된 선택입니다. 프로그램을 종료합니다.")