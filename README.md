# 성적 CSV 검증 프로그램 (load_scores)

## ① 무엇을 하나요 (What)

성적 CSV 파일을 읽어 0~100점 사이의 유효한 데이터만 걸러내고, 규칙을 어긴 줄은 사유와 함께 기록하는 프로그램입니다.

## ② 왜 만들었나요 (Why)

실제 성적 CSV 파일에는 빈 줄, 점수 누락, 0~100 범위 밖 점수, 열 개수 오류 등이 섞여 있어 그대로 읽으면 프로그램이 멈추거나 잘못된 값이 들어가기 때문에, 예외를 안전하게 처리하고 검증까지 자동화하기 위해 만들었습니다.

## ③ 어떻게 쓰나요 (How)

```bash
# 설치
pip install pytest pytest-cov

# 실행
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

| 파일 | 하는 일 |
| --- | --- |
| load_scores.py | 성적 CSV 파싱 및 검증 프로그램 |
| test_load_scores.py | 정상·예외·경계값·빈 이름 검증 pytest 코드 |
| scores.csv | 테스트용 성적 데이터 |
| empty.csv | 헤더만 있는 테스트 파일 |
| README.md | 프로젝트 설명서 |
| LICENSE | MIT 라이선스 |

## ⑥ 만든 사람 · AI를 어디에 썼는지

- 만든 사람 : 하헌진 (2026100282)
- AI를 쓴 곳 : STEP 3 비교 실험(코드·명세·버그 코드 기반 AI 테스트 생성 및 비교)과 pytest 문법 확인
- 내가 직접 판단한 것 : 명세서 6칸 기반 8개 테스트 케이스 설계 및 test_load_scores.py 직접 작성, 커버리지 미실행 줄(55~56번 줄) 분석 후 빈 이름 테스트 추가, 3회 분할 커밋 및 README 작성

## 라이선스

MIT License (LICENSE 파일 참고)
