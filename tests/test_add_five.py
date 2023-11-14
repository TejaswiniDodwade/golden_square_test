from lib.add_five import*

def test_add_five_returns_eight_for__three():
    result = add_five(3)
    assert result == 8