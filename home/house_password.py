#!/usr/bin/env checkio --domain=py run house-password

# 
# END_DESC

def checkio(data):

    """The password will be considered strong enough if its length is
        1. greater than or equal to 10 symbols
        2. it has at least one digit
        3. as well as containing one uppercase letter and one lowercase letter in it. The password contains only ASCII latin letters or digits."""
    cond1 = len(data) >= 10
    cond2 = any(c.isdigit() for c in data)
    cond3 = not any([data.isdigit(), data.islower(), data.isupper()])

    return all([cond1, cond2, cond3])

# Some hints
# Just check all conditions


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert checkio(u'A1213pokl') == False, "1st example"
    assert checkio(u'bAse730onE4') == True, "2nd example"
    assert checkio(u'asasasasasasasaas') == False, "3rd example"
    assert checkio(u'QWERTYqwerty') == False, "4th example"
    assert checkio(u'123456123456') == False, "5th example"
    assert checkio(u'QwErTy911poqqqq') == True, "6th example"