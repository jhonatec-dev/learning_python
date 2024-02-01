def division(nums):
    try:
        div = 1
        for key, value in enumerate(nums):
            if key == 0:
                div = value
            else:
                div /= value
        return div
    except ZeroDivisionError:
        return 0


def test_division():
    assert division([1, 2, 3]) == 0


def test_division_by_zero():
    assert division([1, 0]) == 0
