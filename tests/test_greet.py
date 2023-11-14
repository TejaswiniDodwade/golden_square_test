from lib.greet import *

def test_greet_with_name():
    result = greet("Tina")

    assert result == "Hello, Tina!"
