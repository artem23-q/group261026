from utils.numbers_utils import is_number_bigger_than_10

def test_is_number_bigger_than_10():
    number = 9
    expected = False
    actual = is_number_bigger_than_10(number)
    assert expected is actual

def test_is_number_bigger_than_10_case2():
    number = 10
    expected = False
    actual = is_number_bigger_than_10(number)
    assert expected is actual

def test_is_number_bigger_than_10_case3():
    number = 101
    expected = True
    actual = is_number_bigger_than_10(number)
    assert expected is actual

def test_is_number_bigger_than_10_case4():
    number = 10.5
    expected = True
    actual = is_number_bigger_than_10(number)
    assert expected is actual

def test_is_number_bigger_than_10_case5():
    number = -10
    expected = False
    actual = is_number_bigger_than_10(number)
    assert expected is actual