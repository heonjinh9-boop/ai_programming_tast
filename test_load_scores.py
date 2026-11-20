import pytest
from load_scores import load_scores


def test_정상_파일을_읽는다():
    kept, skipped = load_scores("scores.csv")
    assert len(kept) == 5


def test_빈_줄은_건너뛴다(tmp_path):
    p = tmp_path / "blank.csv"
    p.write_text("name,score\n\n김하나,88\n\n이둘,92\n", encoding="utf-8")
    kept, skipped = load_scores(p)
    assert kept == [("김하나", 88), ("이둘", 92)]
    assert skipped == []


def test_이름에_쉼표가_있어도_읽는다(tmp_path):
    p = tmp_path / "comma.csv"
    p.write_text('name,score\n"김,하나",88\n', encoding="utf-8")
    kept, skipped = load_scores(p)
    assert kept == [("김,하나", 88)]
    assert skipped == []


def test_없는_파일이면_오류가_난다():
    with pytest.raises(FileNotFoundError):
        load_scores("없는파일.csv")


def test_헤더만_있으면_빈_결과가_나온다():
    kept, skipped = load_scores("empty.csv")
    assert kept == []
    assert skipped == []


@pytest.mark.parametrize("점수, 유효한가", [
    (-1, False),
    (0, True),
    (1, True),
    (99, True),
    (100, True),
    (101, False),
])
def test_점수_경계값(tmp_path, 점수, 유효한가):
    p = tmp_path / "boundary.csv"
    p.write_text(f"name,score\n테스트,{점수}\n", encoding="utf-8")
    kept, skipped = load_scores(p)
    assert (len(kept) == 1) == 유효한가