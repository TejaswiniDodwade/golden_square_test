from lib.gratitudes import *

def test_gratitude():
    gratitude = Gratitudes()
    gratitude.add("Good Health")
    assert gratitude.gratitudes[-1] == "Good Health"
    formatted_result = gratitude.format()
    assert formatted_result == "Be grateful for: Good Health"
    
    
