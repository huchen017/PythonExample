import pytest
from pytesttraining.myapp import add


@pytest.fixture()
def loginandlogout():
    print("I am login")
    yield
    print("I am logout")

class TestSample:
    @pytest.mark.usefixtures("loginandlogout")
    def test_answer1(self):
       assert add.add_method(1,2) == 3

    @pytest.mark.usefixtures("loginandlogout")
    def test_answer2(self):
       assert add.add_method(1,2) == 3
