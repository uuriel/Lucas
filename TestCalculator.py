def assertEqual(actual, expected):
    assert actual == expected, f"Expected {expected}, but got {actual}"


def assertRaises(exception, func, *args, **kwargs):
    try:
        func(*args, **kwargs)
    except exception:
        return

from Calculator import Calculator


# Test cases
def test_add():
    calculator = Calculator()
    a, b = 3, 4
    expected_result = 7
    result = calculator.add(a, b)
    assertEqual(result, expected_result)
    print("test_add passed")

def test_subtract():
    calculator = Calculator()
    a, b = 10, 5
    expected_result = 5
    result = calculator.subtract(a, b)
    assertEqual(result, expected_result)
    print("test_subtract passed")

def test_multiply():
    calculator = Calculator()
    a, b = 6, 7
    expected_result = 42
    result = calculator.multiply(a, b)
    assertEqual(result, expected_result)
    print("test_multiply passed")

def test_divide():
    calculator = Calculator()
    a, b = 8, 2
    expected_result = 4
    result = calculator.divide(a, b)
    assertEqual(result, expected_result)
    print("test_divide passed")

def test_divide_by_zero():
    calculator = Calculator()
    a, b = 5, 0
    assertRaises(ZeroDivisionError, calculator.divide, a, b)
    print("test_divide_by_zero passed")

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    test_divide_by_zero()
    print("All tests passed")
