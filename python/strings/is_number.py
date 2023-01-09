
def isNumber(s: str) -> bool:
    try:
        x = s.lower()

        # check for infinity as it's a valid number in python
        if x in ['inf', '+inf', '-inf', 'infinity', '-infinity', '+infinity']:
            return False

        # convert to float
        float(s)
        return True
    except:
        return False


s = "0"
print('{} is{} a Number'.format(s, '' if isNumber(s) else ' not'))
