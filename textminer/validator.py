import re
# @xfail
# def test_words():
#     """words can take an optional count argument. In case it exists, the text
#     must match that number of words."""
#     assert v.words("hello")
#     assert v.words("hello world")
#     assert v.words("raggggg hammer dog")
#     assert v.words("18-wheeler tarbox")
#     assert v.words("hello", count=1)
#     assert v.words("hello world", count=2)
#     assert v.words("raggggg hammer dog", count=3)
#     assert v.words("18-wheeler tarbox", count=2)
#     assert not v.words("")
#     assert not v.words("12")
#     assert not v.words("hey !!!", count=2)
#     assert not v.words("bar*us w!zard", count=2)
#     assert not v.words("hello", count=2)
#     assert not v.words("hello world", count=3)
#     assert not v.words("raggggg hammer dog", count=1)
#     assert not v.words("18-wheeler tarbox", count=3)





def binary(text):
    return re.match(r'[01]', text)

def binary_even(text):
    return re.match(r'[01]+0$', text)

def hex(text):
    return re.match(r'[\dA-F]+$', text)

def word(text):
    return re.match(r'[18a-zA-Z-]+$', text)

# def words(text, count = None):
#     a_list = re.findall(r'[18a-zA-Z-\s]', text)
#     if count:
#         return re.search(r'[18a-zA-Z-\s]', text), len(a_list)
#     else:
#         return re.search(r'[18a-zA-Z-\s]', text)
