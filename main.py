from filter import filter_text
from stats import save_log, show_stats, get_top_badwords

def main():
    print("🐹 귀여운 욕설 차단기 시작! (quit 입력 시 종료)")

    # 👉 인터넷 밈 스타일 톤 선택
    print("\n🔥 오늘의 밈(?) 톤을 골라보세요 🔥")
    tones = {
        "1": ("cute", "🐹 애교만땅 햄찌 (\"ㅇㅅㅇ 뿌잉뿌잉\")"),
        "2": ("polite", "👔 매너가 사람을 만든다 (\"고객님, 진정하시죠\")"),
        "3": ("cynical", "😒 시니컬 고양이 (\"니맘 알빠노\")")
    }

    for key, (_, desc) in tones.items():
        print(f"[{key}] {desc}")

    choice = input("👉 번호를 입력 (아무거나 치면 1번행 ㅋㅋ): ")

    # 👉 선택한 톤 (기본값은 1번 cute)
    tone, tone_desc = tones.get(choice, tones["1"])

    print(f"\n✨ 선택 완료: {tone_desc} ✨\n")

    # 👉 본격 실행 (단순화 + 원본/변환 + 톤 표시)
    while True:
        text = input("\n💬 변환할 문장을 입력하세요 (엔터 또는 quit 입력 시 종료): ")

        # 👉 종료 조건
        if text.strip() == "" or text.lower() == "quit":
            print("\n📊 프로그램을 종료합니다. 아래에서 기록을 확인하세요!\n")
            break

        # 👉 욕 변환 실행
        result = filter_text(text, tone)

        # 👉 결과 출력 (원본 + 변환 + 톤)
        print("\n--- 변환 결과 ---")
        print(f"원본 : {text}")
        print(f"변환 : {result} 💖")
        print(f"톤   : {tone_desc}")
        print("----------------\n")

        save_log(text, result)

    # 👉 기본 통계 출력
    show_stats()

    # 👉 오늘의 욕 TOP3 출력
    top3 = get_top_badwords(3)
    if top3:
        print("\n🔥 오늘의 욕 TOP3 🔥")
        for i, (word, count) in enumerate(top3, start=1):
            print(f"{i}. {word} ({count}회)")
    else:
        print("\n오늘은 욕이 감지되지 않았습니다. 클린한 하루~ ✨")

if __name__ == "__main__":
    main()
