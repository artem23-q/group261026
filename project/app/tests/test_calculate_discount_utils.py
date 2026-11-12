from utils.calculate_discount_utils import calculate_discount

def test_calculate_discount_20():
    price = 100
    discount = 20
    expected = 80
    actual = calculate_discount(price, discount)
    assert actual == expected

def test_calculate_discount_50():
    price = 100
    discount = 50
    expected = 50
    actual = calculate_discount(price, discount)
    assert actual == expected

def test_calculate_discount_0():
    price = 100
    discount = 0
    expected = 100
    actual = calculate_discount(price, discount)
    assert actual == expected

def test_calculate_price_0():
    price = 0
    discount = 20
    expected = 0
    actual = calculate_discount(price, discount)
    assert actual == expected

def test_calculate_custom():
    price = 70
    discount = 20
    expected = 56
    actual = calculate_discount(price, discount)
    assert actual == expected