# 성적 CSV 검증 프로그램 (load_scores)

## ① 무엇을 하나요 (What)

성적 CSV 파일을 읽어서 0~100점 사이의 정상 데이터만 골라내고, 잘못된 줄은 이유와 함께 따로 기록하는 프로그램입니다.

## ② 왜 만들었나요 (Why)

실제 CSV 파일에는 빈 줄이나 빠진 점수, 0~100 범위를 벗어난 값, 열 개수가 안 맞는 줄이 섞여 있는 경우가 많습니다. 그냥 읽으면 프로그램이 중간에 멈추거나 잘못된 점수가 들어가기 때문에, 오류 줄을 안전하게 걸러내고 테스트로 확인하기 위해 만들었습니다.

## ③ 어떻게 쓰나요 (How)

```bash
pip install pytest pytest-cov
python load_scores.py scores.csv
```

## ④ 어떻게 테스트하나요

```bash
pytest test_load_scores.py
pytest test_load_scores.py --cov=load_scores --cov-report=term-missing
```

```
12 passed in 0.05s
```

## ⑤ 파일 구성

- load_scores.py : 성적 CSV를 읽고 유효한 점수와 건너뛴 줄을 나누는 코드
- test_load_scores.py : 정상, 예외, 경계값, 빈 이름 처리를 확인하는 pytest 테스트 코드
- scores.csv : 정상 데이터와 오류 데이터가 섞인 테스트용 CSV 파일
- empty.csv : 헤더만 들어 있는 예외 확인용 CSV 파일
- README.md : 프로그램 설명과 실행 방법을 적은 문서
- LICENSE : MIT 라이선스 파일

## ⑥ 만든 사람 · AI를 어디에 썼는지

- 만든 사람 : 하헌진 (2026100282)
- AI를 쓴 곳 : STEP 3 비교 실험(코드, 명세, 버그 코드로 테스트 생성 비교)과 pytest 문법 확인
- 내가 직접 판단한 것 : 명세서 6칸을 보고 테스트 케이스 8개 설계, test_load_scores.py 작성, 커버리지에서 안 지나간 55~56번 줄 확인 후 빈 이름 테스트 추가, 3번 나눠 커밋 및 README 작성

## 라이선스

MIT License (LICENSE 파일 참고)