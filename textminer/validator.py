import re

def binary(text):
    return re.match(r'[01]', text)

def binary_even(text):
    return re.match(r'[01]+0$', text)

def hex(text):
    return re.match(r'[\dA-F]+$', text)

def word(text):
    return re.match(r'[18a-zA-Z-]+$', text)

def words(text, count=None):
    matches = re.findall(r'[\w-]+[a-zA-Z]+', text)
    if count is not None:
        return len(matches) == count
    else:
        return len(matches) > 0

def phone_number(text):
    return re.match(r'[\d\W]{3}?[\d\W]{3}?[\d\W]{4}?', text)

def money(text):
    return re.match(r'^\$([0-9]{1,3})(,?[0-9]{3})*(\.[0-9]{2})?$', text)

def zipcode(text):
    return re.match(r'^([0-9]{5})(\-[0-9]{4})?$', text)

def date(text):
    return re.match(r'[0-9]{1,4}[\/-][0-9]{1,2}[\/-][0-9]{2,4}', text)

#ADVANCE MODE BEGINS#
