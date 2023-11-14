import pytest
from lib.present import *

def test_wrapping_and_unwrapping():
    present_1 = Present()
    present_1.wrap("I like dog")
    result = present_1.unwrap()
    assert result == "I like dog"

def test_unwrapping():
    present_1 = Present()
    with pytest.raises(Exception) as e:
        present_1.unwrap()
    error_message = str(e.value) 
    assert error_message == "No contents have been wrapped."

def test_wrapping_twice():
    present_1 = Present()
    present_1.wrap("kskjkjncdkd")
    with pytest.raises(Exception) as e:
        present_1.wrap("jsidjskdjskjs")
    error_message = str(e.value) 
    assert error_message == "A contents has already been wrapped."
    