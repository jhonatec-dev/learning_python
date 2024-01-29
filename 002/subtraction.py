def subtraction(nums):
    sub = 0
    for i in nums:
        sub -= i
    return sub


def test_subtraction():
    assert subtraction([1, 2, 3]) == -6
