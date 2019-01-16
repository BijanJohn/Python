import string

def checkio(text):
    """
    We iterate through latyn alphabet and count each letter in the text.
    Then 'max' selects the most frequent letter.
    For the case when we have several equal letter,
    'max' selects the first from they.

    max is a built in function, https://docs.python.org/3/library/functions.html#max
    import string allows for https://www.geeksforgeeks.org/python-string-ascii_lowercase/
    """
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"