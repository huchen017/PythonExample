from pytesttraining.myapp import pytest_practice
import pytest

@pytest.mark.parametrize("nums,expect_result",[
    ([5,2,45,6,8,2,1],[1,2,2,5,6,45,8]),
    ([5,2,59,6,8,9,1],[1,2,5,6,8,9,59]),
    ([5,2,59,7,10,15,1],[1,2,5,7,10,15,59])
])
def test_bubble_sort(nums,expect_result):
    assert pytest_practice.bubble_sort(nums) == expect_result
