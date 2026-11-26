from decorators.decoratore import add, greeting, multiply

def test_add():
    assert add(1, 2) == {
            'result': 3,
            'status': 'success'
    }

def test_greeting():
    assert greeting("John") == {
            'result': "Hello, John!",
            'status': 'success'
        }

def test_multiply():
    assert multiply(2, 3) == {
            'result': 6,
            'status': 'success'
    }