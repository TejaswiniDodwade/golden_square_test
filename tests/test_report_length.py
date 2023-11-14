from lib.report_length import *

def test_report_length_for_string():
    result = report_length("Tejaswini")
    assert result == "This string was 9 characters long."