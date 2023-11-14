from lib.counter import *

def counter_to_count():
    counter = Counter
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 5 so far."