
# 귀여운 욕설 필터

## 주요 기능
- 욕설 단어를 랜덤한 대체어로 변환
    - 대체어 목록: "유니콘🦄", "무지개🌈", "햇살🔆", "꽃🌻", "별✨", "사랑💖", "희망🌱", "비눗방울🫧", "바다🌊", "숲🌳"

    
- 욕설 사용 횟수가 0번, 5번 이하, 6번 이상 때 마다 다른 격려 메시지 출력
    - 0번 : 바르고 고운 말만 사용했어요! 칭찬해요 💖
    - 5번 이하: 욕설을 조금만 사용했어요! 앞으로도 응원해요 🐹
    - 6번 이상: 욕이 조금 많았어요ㅠㅠ 더 조심히 말해보아요! 💪
  

<br><br><br>
## 실행 화면

### <br>1. 잘못된 입력 시 화면
<img width="576" height="288" alt="Image" src="https://github.com/user-attachments/assets/78946ce1-bbf7-46ff-91c4-01e6abc84f6b" />

### <br>2. log 기록 화면
<img width="1005" height="817" alt="Image" src="https://github.com/user-attachments/assets/24c78d8f-fcbe-4a8c-9e70-a8be9e14f25f" />

### <br>3. 욕설 사용 횟수별 격려화면

#### 1) 0번
<img width="1047" height="850" alt="Image" src="https://github.com/user-attachments/assets/3fd01a26-b3b8-460e-9021-7fe3e7cf3c5e" />

#### 2) 5회 이하
<img width="1047" height="860" alt="Image" src="https://github.com/user-attachments/assets/766b6219-7e4f-4515-a9bd-44dbdf9dcc68" />

#### 6) 6회 이상
<img width="1047" height="851" alt="Image" src="https://github.com/user-attachments/assets/8e150ed5-4e6f-4c52-8d7f-a871189db3de" />



 ### 참고 사항
- `tone_dict.json`이 없으면 경고 메시지 출력
- 로그 파일이 없으면 자동 생성
- 로그에는 욕설 감지 전 원문과 변환 결과 모두 기록
- 욕설 리스트는 "리그오브레전드_필터링리스트)2020.txt"를 Json 파일로 변환해서 사용(저작권 관련 찾아볼 필요 ㅇ) 



