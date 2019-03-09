import pytest

@pytest.fixture()
def loginandlogout():
    print("I am login")
    yield
    print("I am logout")

class TestSample1:
    def test_answer1(self,loginandlogout):
        print("test_answer1")

    def test_answer2(self,loginandlogout):
        print("test_answer2")

class TestSample2:
    def test_answer3(self,loginandlogout):
        print("test_answer3")

    def test_answer4(self,loginandlogout):
        print("test_answer4")