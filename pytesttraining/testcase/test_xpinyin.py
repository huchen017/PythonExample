import pytest
from pytesttraining.xpinyin import Pinyin


@pytest.mark.parametrize("chars,splitter,tone_marks,convert,expectresult", [
    ("武汉", "-", "marks", "lower", "wuhan")])
def test_get_pinyin(chars,splitter,tone_marks,convert,expectresult):
    assert Pinyin().get_pinyin(chars=chars, splitter=splitter, tone_marks=tone_marks, convert=convert) == expectresult
