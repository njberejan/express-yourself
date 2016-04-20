import re

def words(text):
    return re.findall(r'^[18a-zA-Z-\s]+$', text)
    """no idea why this doesn't work."""

def phone_numbers(text):
    return re.compile()




# @xfail
# @params("input,expected", [
#     ("919-555-1212", {"area_code": "919", "number": "555-1212"}),
#     ("(919) 555-1212", {"area_code": "919", "number": "555-1212"}),
#     ("9195551212", {"area_code": "919", "number": "555-1212"}),
#     ("919.555.1212", {"area_code": "919", "number": "555-1212"}),
#     ("919 555-1212", {"area_code": "919", "number": "555-1212"}),
#     ("555-121", None)
# ])
def test_phone_numbers(input, expected):
    assert s.phone_number(input) == expected
