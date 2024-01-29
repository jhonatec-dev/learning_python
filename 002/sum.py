def sum(nums):
    sum = 0
    for i in nums:
        sum += i
    return sum


def test_sum():
    assert sum([1, 2, 3]) == 6
