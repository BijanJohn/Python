from itertools import groupby

def long_repeat(text):
    return max([len(list(g)) for k, g in groupby(text)], default=0)

if __name__ == '__main__':
    # These "asserts" using only for self-checking
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    assert long_repeat('aaaaabbbbbbeeebbffffffffff') == 10, "My assertion"
    print('Checks out solid!')