import pytest


@pytest.fixture(autouse=False)
def connectdb():
    print("connect db")
    yield
    print("unconnect db")