def multiplication(nums):
    mul = 1
    for i in nums:
        mul *= i
    return mul


def test_multiplication():
    assert multiplication([1, 2, 3]) == 6
