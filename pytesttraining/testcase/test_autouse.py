import pytest
from pytesttraining.myapp import add


@pytest.fixture(scope="module",autouse=True)
def loginandlogout():
    print("I am login")
    yield
    print("I am logout")

@pytest.fixture(scope="class",autouse=True)
def click_login():
    print("click_login")
    yield
    print("click_logout")

class TestSample:
    def test_answer1(self):
        print("test_answer1")
        assert add.add_method(1,2) == 3

    def test_answer2(self):
        print("test_answer2")
        assert add.add_method(1,2) == 3
