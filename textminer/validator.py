import re

# @xfail
# def test_binary_even():
#     """String must be a binary number and be even."""
#
#     assert v.binary_even("10")
#     assert v.binary_even("1110100010")
#     assert not v.binary_even("1011")

def binary(text):
    return re.match(r'[01]', text)

def binary_even(text):
    return re.match(r'[01]+0$', text)
