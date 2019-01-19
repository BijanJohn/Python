def long_repeat(text):
    if text == "":
        return 0
    counter = 0
    text_l = text.lower()
    max_counter = 0                                   # add

    for i in range(len(text_l) - 1):
        if text_l[i] == text_l[i+1]:
            counter += 1
        else:                                         # add
            max_counter = max(max_counter, counter+1) # add
            counter = 0                               # add

    return max(max_counter, counter+1)                # update
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    assert long_repeat('aaaaabbbbbbeeebbffffffffff') == 10, "My assertion"
    print('Checks out solid!')