from lib.string_builder import *

def test_string_builder_length():
    string_builder = StringBuilder()
    string_builder.add("Tejaswini")
    assert string_builder.output() == "Tejaswini"
    assert string_builder.size() == 9
   
    