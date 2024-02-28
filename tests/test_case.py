import python_code

def test_add():
    assert python_code.add(1, 2) == 3
    assert python_code.add(5, 7) == 12

def test_subtract():
    assert python_code.subtract(5, 2) == 3
    assert python_code.subtract(10, 7) == 3
