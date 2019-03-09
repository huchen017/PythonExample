from pytesttraining.myapp import add
import pytest

@pytest.mark.parametrize("x,y",[
    (4,8),
    (6,8),
    (1+2,9)
])
def test_add(x,y):
    assert add.add_method(x,y)==x+y